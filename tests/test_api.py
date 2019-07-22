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
    'product_name': 'chuheyihao',
    'date': '2019-07-20',
    'unit_value': 1.0402,
    'asset_value': 12321983.98,
    'shares': 10000000,
    'unit_value_change': 0.0057,
    'asset_value_change': -12721.27,
    'note_of_important_events': ''      # If needed
}

post_daily_product_performance_data(data, to_localhost=True)
