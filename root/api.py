from root import *
from flask import request


"""---------------------------------  Interactive API Definition ---------------------------------"""


@app.route('/api/v1/performance/<string:product_name>', methods=['GET'])
def check_product_performance(product_name):
    cursor = conn.cursor()
    query = 'SELECT date, unit_value FROM product_performance_{} ORDER BY date;'.format(product_name)
    success_code = 0
    dates = []
    unit_values = []
    try:
        cursor.execute(query)
        for row in cursor.fetchall():
            dates.append(row[0].strftime('%Y-%m-%d'))
            unit_values.append(row[1])
        success_code = 1
    except Exception as e:
        print('Error: ', e)
        cursor.execute('rollback')
    finally:
        return jsonify({'success_code': success_code,
                        'dates': dates,
                        'unit_values': unit_values})


@app.route('/api/v1/performance/<string:product_name>/update', methods=['POST'])
def update_product_performance(product_name):
    print('The user has updated the product: {}'.format(product_name))
    print(request.get_data())
    return redirect('/api/v1/performance/{}'.format(product_name))
