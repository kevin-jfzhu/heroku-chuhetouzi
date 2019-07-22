from root.utils import app, redirect, jsonify
from root.utils.db_setup import *
from flask import request
import calendar, time, datetime


"""---------------------------------  Interactive API Definition ---------------------------------"""


@app.route('/api/v1/performance/<string:product_name>', methods=['GET'])
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
        return redirect('/api/v1/performance/{}'.format(data.get('product_name')))


'''
@app.route('/api/v1/performance/<string:product_name>/update', methods=['POST'])
def update_product_performance(product_name):
    print('The user has updated the product: {}'.format(product_name))
    try:
        data = request.get_json()
        if data.get('date') is not None:
            search_date = data.get('date')
            cursor = conn.cursor()
            query = "SELECT date FROM product_performance_{} WHERE date = '{}';".format(product_name, str(search_date))
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.execute('rollback')

            # If the record in the given day doesn't exist, then insert a new records with the value
            if len(results) == 0:
                query = """
                        INSERT INTO product_performance_{}
                            (date, unit_value, asset_value, shares, unit_value_change,
                            asset_value_change, note_of_important_events)
                        VALUES
                            ('{}', {}, {}, {}, {}, {}, '{}');
                        """.format(
                                product_name,
                                data.get('date'),
                                data.get('unit_value'),
                                data.get('asset_value'),
                                data.get('shares'),
                                data.get('unit_value_change'),
                                data.get('asset_value_change'),
                                data.get('note_of_important_events'),
                            )
                print('Data has been inserted as: ' + str(data))
                cursor.execute(query)

            # If the record in the given day exists, then update the records with the new value
            elif len(results) > 0:
                query = """
                        UPDATE product_performance_{}
                            SET
                                unit_value = {},
                                asset_value = {},
                                shares = {},
                                unit_value_change = {},
                                asset_value_change = {},
                                note_of_important_events = '{}'
                            WHERE date = '{}';
                        """.format(product_name,
                                   data.get('unit_value'),
                                   data.get('asset_value'),
                                   data.get('shares'),
                                   data.get('unit_value_change'),
                                   data.get('asset_value_change'),
                                   data.get('note_of_important_events'),
                                   data.get('date'))
                cursor.execute(query)
                print('Data has been updated as: ' + str(data))

            cursor.close()

    except Exception as e:
        raise ValueError('Cannot update data, since: ', e)

    finally:
        return redirect('/api/v1/performance/{}'.format(product_name))
'''
