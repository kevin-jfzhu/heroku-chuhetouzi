import requests
import json
import csv
import time


def post_dxp_performance_data(daily_performance_data, to_localhost=False):
    if to_localhost:
        domain = 'http://127.0.0.1:5000'
    else:
        domain = 'http://chuhetouzi.herokuapp.com'

    post_uri = domain + '/api/v1/strategy/dxp/update'
    try:
        r = requests.post(post_uri, json=daily_performance_data)
        if r.status_code != 200:
            raise IOError('Status code error: code = {}'.format(str(r.status_code)))
        else:
            print('Data has been posted as: ' + daily_performance_data['date'])
    except Exception as e:
        print('Fail to post the data, exception as:')
        print(e)


def import_dxp_performance_data_from_csv(csvfilename, encoding='utf-8'):
    results = []
    with open(csvfilename, 'r+', encoding=encoding, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data = {
                'date': row['date'],
                'subclass_name': row['subclass_name'],
                'strategy_value': row['strategy_value'],
                'holding_shares': row['holding_shares'],
                'signal_direction': row['signal_direction'],
                'correct_direction': row['correct_direction'],
                'rolling_accuracy': row['rolling_accuracy'],
                'trailing_drawdown': row['trailing_drawdown'],
                'note_of_important_events': ''  # If needed
            }
            post_dxp_performance_data(data, to_localhost=True)
            time.sleep(0.2)


if __name__ == '__main__':

    # UPDATE DATA HERE
    data = {
        'date': '2015/4/15',
        'subclass_name': 'fast',
        'strategy_value': 2800081.136,
        'holding_shares': 0,
        'signal_direction': 1,
        'correct_direction': -1,
        'rolling_accuracy': 0,
        'trailing_drawdown': -0.066639621,
        'note_of_important_events': ''      # If needed
    }

    post_dxp_performance_data(data, to_localhost=True)
