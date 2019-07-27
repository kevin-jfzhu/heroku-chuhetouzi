import requests


def post_daily_product_performance_data(daily_performance_data, to_localhost=False):
    if to_localhost:
        domain = 'http://127.0.0.1:5000'
    else:
        domain = 'http://chuhetouzi.herokuapp.com'

    post_uri = domain + '/api/v1/performance/product/update'
    try:
        r = requests.post(post_uri, json=daily_performance_data)
        if r.status_code != 200:
            raise IOError('Status code error: code = {}'.format(str(r.status_code)))
        else:
            print('Data has been posted')
    except Exception as e:
        print('Fail to post the data, exception as:')
        print(e)


# UPDATE DATA HERE
data = {
    'product_name': 'test',
    'date': '2019-07-22',
    'unit_value': 1.0253,
    'asset_value': 11170230.86,
    'shares': 10927097,
    'unit_value_change': 0.0052,
    'asset_value_change': 56767.04,
    'note_of_important_events': ''      # If needed
}

post_daily_product_performance_data(data, to_localhost=True)
