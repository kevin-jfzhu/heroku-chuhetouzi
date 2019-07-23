from root.utils import app, redirect, jsonify
from root.utils.db_setup import *
from flask import request
import calendar, time, datetime


"""---------------------------------  Interactive API Definition ---------------------------------"""


# 产品净值相关API
@app.route('/api/v1/performance/product/<string:product_name>', methods=['GET'])
def check_product_performance(product_name):
    success_code = 0
    dates = []
    unit_values = []
    try:
        results = session.query(ProductPerformance)\
                    .filter_by(product_name=product_name)\
                    .order_by(ProductPerformance.date)\
                    .all()
        for item in results:
            dates.append(item.date.strftime('%Y-%m-%d'))
            unit_values.append(item.unit_value)
        success_code = 1
    except Exception as e:
        session.rollback()
        print('Error: ', e)
    finally:
        return jsonify({'success_code': success_code,
                        'dates': dates,
                        'unit_values': unit_values})


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
                pp = ProductPerformance(last_updated_time = int(time.time()),
                                        date = data.get('date'),
                                        product_name = data.get('product_name'),
                                        unit_value = data.get('unit_value'),
                                        asset_value = data.get('asset_value'),
                                        unit_value_change = data.get('unit_value_change'),
                                        asset_value_change = data.get('asset_value_change'),
                                        shares = data.get('shares'),
                                        note_of_important_events = data.get('note_of_important_events')
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
        today = datetime.datetime.today()
        results = session.query(StrategyPerformance)\
                    .filter_by(subclass_name=subclass_name)\
                    .filter(StrategyPerformance.date >= '2016-01-01') \
                    .filter(StrategyPerformance.date < today) \
                    .order_by(StrategyPerformance.date)\
                    .all()
        if len(results) > 0:
            start_point = results[0].strategy_value
            for row in results:
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
                sp = StrategyPerformance(last_updated_time=int(time.time()),
                                         date=data.get('date'),
                                         subclass_name=data.get('subclass_name'),
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
