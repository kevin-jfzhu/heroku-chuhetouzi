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


# 大小盘策略相关API
@app.route('/api/v1/strategy/dxp/<string:subclass_name>', methods=['GET'])
def check_daxiaopan_performance(subclass_name):
    success_code = 0
    r = {
        'strategy_name': 'daxiaopan',
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
        results = session.query(DaXiaoPan)\
                    .filter_by(subclass_name=subclass_name)\
                    .order_by(DaXiaoPan.date)\
                    .all()
        for row in results:
            r['dates'].append(row.date)
            r['strategy_values'].append(row.strategy_value)
            r['holding_shares'].append(row.holding_shares)
            r['signal_directions'].append(row.signal_direction)
            r['correct_directions'].append(row.correct_direction)
            r['rolling_accuracies'].append(row.rolling_accuracy)
            r['trailing_drawdowns'].append(row.trailing_drawdown)
            r['note_of_important_events'].append(row.note_of_important_events)
        success_code = 1
    except Exception as e:
        session.rollback()
        print('Error: ', e)
    finally:
        return jsonify({'success_code': success_code,
                        'results': r})


@app.route('/api/v1/strategy/dxp/update', methods=['POST'])
def update_daxiaopan_performance():
    try:
        data = request.get_json()
        print('The user is requesting to update the daxiaopan-subclass: {}'.format(data.get('subclass_name')))
        if data.get('date') is not None:
            record = session.query(DaXiaoPan).\
                                filter_by(subclass_name=data.get('subclass_name'), date=data.get('date')).\
                                order_by(DaXiaoPan.date).\
                                first()
            if record is None:
                sp = DaXiaoPan(last_updated_time=int(time.time()),
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
        return "DaXiaoPan strategy performance data has been updated."
