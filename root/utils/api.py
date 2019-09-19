from root.utils import app, redirect, jsonify
from root.utils.db_setup import *
from functools import wraps
from flask import request, make_response
from flask import session as flask_session
import calendar, time, datetime
import os

"""---------------------------------  Login Decorator ---------------------------------"""
app.config['SECRET_KEY'] = os.urandom(24)
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        cur_cookies = request.cookies
        if cur_cookies.get('name') not in flask_session:
            return jsonify({'success_code': 0, 'results': {}})
        return func(*args, **kwargs)
    return decorated_function


"""---------------------------------  Interactive API Definition ---------------------------------"""
# 登陆相关API
@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        user = session.query(ChtzUser)\
                .filter_by(username=username)\
                .first()
        if user is not None and request.form['password'] == user.password:
            response = make_response(jsonify({'success_code': 1, 'results': {}}))
            response.set_cookie('name', username, expires=datetime.datetime.today() + datetime.timedelta(days=30))
            flask_session[username] = 1
            return response
    return jsonify({'success_code': 0, 'results': {}})


# 仓位数据相关API
@app.route('/api/v1/performance/product/<string:product_name>/detail', methods=['POST', 'GET'])
@login_required
def check_product_position_detail(product_name):
    success_code = 0
    #strategies = ['bigsmall_fast', 'bigsmall_vol', 'bigsmall_ensemble', 'bigsmall_sentim', 'index-timing_general', 'index-timing_ensemble', 'flow-sentim_low']
    strategy_map = {
            'bigsmall_fast': r'大小盘(快)',
            'bigsmall_ensemble': r'大小盘(集成)',
            'bigsmall_vol': r'大小盘(带量)',
            'bigsmall_slow': r'大小盘(慢)',
            'bigsmall_sentim': r'大小盘(资金情绪)',
            'index-timing_general': r'指数择时',
            'index-timing_ensemble': r'指数择时(集成)',
            'flow-sentim_mid': r'资金情绪(中波)',
            'flow-sentim_low': r'资金情绪(低波)'
        }
    r = {
        'dates': [],
        'unit_values': [],
        'series_dict': {}
    }
    try:
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        if request.args.get('start_date') is None:
            start_date = (datetime.datetime.today() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
        else:
            start_date = request.args.get('start_date')

        position_results = session.query(ProductPositionDetail)\
                        .filter(ProductPositionDetail.date >= start_date) \
                        .filter(ProductPositionDetail.date < today) \
                        .filter(ProductPositionDetail.__dict__[product_name].isnot(None)) \
                        .order_by(ProductPositionDetail.date)\
                        .all()

        if position_results:
            start_date = position_results[0].date
            product_results = session.query(ProductPerformance)\
                        .filter_by(product_name=product_name) \
                        .filter(ProductPerformance.date >= start_date) \
                        .filter(ProductPerformance.date < today) \
                        .order_by(ProductPerformance.date) \
                        .all()
                        
            temp_pd, temp_uv = position_results[0].__dict__[product_name].split(';')
            chg_fix = float(product_results[0].unit_value)-float(temp_uv.split(':')[1])
            for pd in temp_pd.split(','):
                strategy, val = pd.split(':')
                r['series_dict'][strategy_map[strategy]] = []
            for item in position_results:
                position_detail_set_str, unit_value_str = item.__dict__[product_name].split(';')
                r['dates'].append(item.date.strftime('%Y-%m-%d'))
                r['unit_values'].append([item.date.strftime('%Y-%m-%d'), float(unit_value_str.split(':')[1])+chg_fix])
                for position_detail_str in position_detail_set_str.split(','):
                    strategy, capital_percent_str = position_detail_str.split(':')
                    r['series_dict'][strategy_map[strategy]].append(float(capital_percent_str)*100)

        success_code = 1
    except Exception as e:
        success_code = -1
        session.rollback()
        print('Error: ', e)
    finally:
        return jsonify({'success_code': success_code,
                        'results': r
                        })


# 产品净值相关API
@app.route('/api/v1/performance/product/<string:product_name>', methods=['GET'])
def check_product_performance(product_name):
    success_code = 0
    r = {
        'product_name': product_name,
        'dates': [],
        'unit_values': [],
        'asset_values': [],
        'note_of_important_events': []
    }
    try:
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        if request.args.get('start_date') is None:
            start_date = (datetime.datetime.today() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
        else:
            start_date = request.args.get('start_date')
        results = session.query(ProductPerformance)\
                    .filter_by(product_name=product_name) \
                    .filter(ProductPerformance.date >= start_date) \
                    .filter(ProductPerformance.date < today) \
                    .order_by(ProductPerformance.date)\
                    .all()
        for item in results:
            r['dates'].append(item.date.strftime('%Y-%m-%d'))
            r['unit_values'].append(item.unit_value)
            r['asset_values'].append(item.asset_value)
            r['note_of_important_events'].append(item.note_of_important_events)
        success_code = 1
    except Exception as e:
        session.rollback()
        print('Error: ', e)
    finally:
        return jsonify({'success_code': success_code,
                        'results': r
                        })


@app.route('/api/v1/performance/product/update', methods=['POST'])
def update_product_performance():
    try:
        data = request.get_json()
        print('The user has updated the product: {}'.format(data.get('product_name')))
        if data.get('date') is not None:
            record = session.query(ProductPerformance).\
                                filter_by(product_name=data.get('product_name'), date=data.get('date')).\
                                order_by(ProductPerformance.date).\
                                first()
            if record is None:
                pp = ProductPerformance(last_updated_time=int(time.time()),
                                        date=data.get('date'),
                                        product_name=data.get('product_name'),
                                        unit_value=data.get('unit_value'),
                                        asset_value=data.get('asset_value'),
                                        unit_value_change=data.get('unit_value_change'),
                                        asset_value_change=data.get('asset_value_change'),
                                        shares=data.get('shares'),
                                        note_of_important_events=data.get('note_of_important_events')
                                        )
                session.add(pp)
                session.commit()
                print('Inserted the new data: ' + str(data))

            else:
                record.last_updated_time = int(time.time())
                record.unit_value = data.get('unit_value')
                record.asset_value = data.get('asset_value')
                record.unit_value_change = data.get('unit_value_change')
                record.asset_value_change = data.get('asset_value_change')
                record.shares = data.get('shares')
                record.note_of_important_events = data.get('note_of_important_events')
                session.add(record)
                session.commit()
                print('Existed record has been updated as: ' + str(data))

    except Exception as e:
        session.rollback()
        raise ValueError('Cannot update data, since: ', e)

    finally:
        return "Product performance data has been updated."


# 策略相关API
@app.route('/api/v1/strategy/<string:subclass_name>', methods=['GET'])
def check_strategy_performance(subclass_name):
    success_code = 0
    r = {
        'strategy_name': subclass_name.split('_')[0],
        'subclass_name': subclass_name,
        'dates': [],
        'strategy_values': [],
        'holding_shares': [],
        'signal_directions': [],
        'correct_directions': [],
        'rolling_accuracies': [],
        'trailing_drawdowns': [],
        'note_of_important_events': []
    }
    try:
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        if request.args.get('start_date') is None:
            start_date = '2016-01-01'
        else:
            start_date = request.args.get('start_date')
        results = session.query(StrategyPerformance)\
                    .filter_by(subclass_name=subclass_name)\
                    .filter(StrategyPerformance.date >= start_date) \
                    .filter(StrategyPerformance.date < today) \
                    .order_by(StrategyPerformance.date)\
                    .all()
        if len(results) > 0:
            start_point = results[0].strategy_value
            for row in results:
                if row.strategy_value is None or row.trailing_drawdown is None:
                    print('NoneType is found: ')
                    print(row)
                r['dates'].append(row.date.strftime('%Y-%m-%d'))
                r['strategy_values'].append(round(row.strategy_value / start_point, 4))
                r['holding_shares'].append(row.holding_shares)
                r['signal_directions'].append(row.signal_direction)
                r['correct_directions'].append(row.correct_direction)
                r['rolling_accuracies'].append(row.rolling_accuracy)
                r['trailing_drawdowns'].append(round(row.trailing_drawdown, 4))
                r['note_of_important_events'].append(row.note_of_important_events)
        success_code = 1
    except Exception as e:
        session.rollback()
        print('Error: ', e)
    finally:
        return jsonify({'success_code': success_code,
                        'results': r})


@app.route('/api/v1/strategy/update', methods=['POST'])
def update_daxiaopan_performance():
    try:
        data = request.get_json()
        print('The user is requesting to update the performance data of strategy: {}'.format(data.get('subclass_name')))
        if data.get('date') is not None:
            record = session.query(StrategyPerformance).\
                                filter_by(subclass_name=data.get('subclass_name'), date=data.get('date')).\
                                order_by(StrategyPerformance.date).\
                                first()
            if record is None:
                sp = StrategyPerformance(date=data.get('date'),
                                         subclass_name=data.get('subclass_name'),
                                         last_updated_time=int(time.time()),
                                         strategy_value=data.get('strategy_value'),
                                         holding_shares=data.get('holding_shares'),
                                         signal_direction=data.get('signal_direction'),
                                         correct_direction=data.get('correct_direction'),
                                         rolling_accuracy=data.get('rolling_accuracy'),
                                         trailing_drawdown=data.get('trailing_drawdown'),
                                         note_of_important_events=data.get('note_of_important_events')
                                         )
                session.add(sp)
                session.commit()
                print('Inserted the new data: ' + str(data))

            else:
                record.last_updated_time = int(time.time())
                record.strategy_value = data.get('strategy_value')
                record.holding_shares = data.get('holding_shares')
                record.signal_direction = data.get('signal_direction')
                record.correct_direction = data.get('correct_direction')
                record.rolling_accuracy = data.get('rolling_accuracy')
                record.trailing_drawdown = data.get('trailing_drawdown')
                record.note_of_important_events = data.get('note_of_important_events')
                session.add(record)
                session.commit()
                print('Existed record has been updated as: ' + str(data))

    except Exception as e:
        session.rollback()
        raise ValueError('Cannot update data, since: ' + e.__str__())

    finally:
        return "Strategy performance data has been updated."


# XWLB相关API
@app.route('/api/v1/special-data/xwlb/<string:name>/<string:sub_type>', methods=['GET'])
def check_xwlb_performance(name, sub_type):
    success_code = 0

    r = {
        'times': [],
        'data': {}, 
        'legends': []
    }
    try:
        target_db = CctvTitle if name=='title' else CctvContent

        if sub_type == 'strd':
            results = session.query(target_db)\
                        .order_by(target_db.date)\
                        .all()
            if len(results) > 0:
                targets = ['No1', 'No2', 'No3', 'No4', 'No5', 'No6', 'No7', 'ZZ500_return_next_week']
                targets_dict = {
                    'No1': 'no1_score',
                    'No2': 'no2_score',
                    'No3': 'no3_score',
                    'No4': 'no4_score',
                    'No5': 'no5_score',
                    'No6': 'no6_score',
                    'No7': 'no7_score',
                    'ZZ500_return_next_week': 'return_500_next_week',
                }

                for target in targets:
                    r['data'][target] = []

                for rel_obj in results:
                    r['times'].append(str(rel_obj.__dict__['date']))
                    for target in targets:
                        r['data'][target].append([str(rel_obj.__dict__['date']), rel_obj.__dict__[targets_dict[target]]])

                r['legends'] = targets
        elif sub_type == 'total':
            results = session.query(target_db)\
                        .order_by(target_db.date)\
                        .all()
            if len(results) > 0:
                bar_targets = ['No1', 'No2', 'No3', 'No4', 'No5', 'No6', 'No7']
                line_targets = ['No1_avg','No2_avg','No3_avg','No4_avg','No5_avg','No6_avg','No7_avg']
                targets_dict = {
                    'No1': 'no1',
                    'No2': 'no2',
                    'No3': 'no3',
                    'No4': 'no4',
                    'No5': 'no5',
                    'No6': 'no6',
                    'No7': 'no7',
                    'No1_avg': 'no1_mean',
                    'No2_avg': 'no2_mean',
                    'No3_avg': 'no3_mean',
                    'No4_avg': 'no4_mean',
                    'No5_avg': 'no5_mean',
                    'No6_avg': 'no6_mean',
                    'No7_avg': 'no7_mean',
                }

                for target in bar_targets+line_targets:
                    r['data'][target] = []

                for rel_obj in results:
                    r['times'].append(str(rel_obj.__dict__['date']))

                    for bar_target in bar_targets:
                        r['data'][bar_target].append(rel_obj.__dict__[targets_dict[bar_target]])

                    for line_target in line_targets:
                        r['data'][line_target].append([str(rel_obj.__dict__['date']), rel_obj.__dict__[targets_dict[line_target]]])

                r['bar_legends']    = bar_targets
                r['line_legends']   = line_targets
                r['legends']        = bar_targets+line_targets

        success_code = 1
    except Exception as e:
        session.rollback()
        print('Error: ', e)
    finally:
        return jsonify({'success_code': success_code,
                        'results': r})
