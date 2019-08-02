# -*- coding: utf-8 -*-
import requests
import pandas as pd
import json


def post_daily_product_performance_data(daily_performance_data, to_localhost=False):
    if to_localhost:
        domain = 'http://127.0.0.1:5000'
    else:
        domain = 'http://chuhetouzi.herokuapp.com'

    #post_uri = domain + '/api/v1/performance/{}/update'.format(product_name)
    post_uri = domain + '/api/v1/strategy/update'
    try:
        r = requests.post(post_uri, json=daily_performance_data)
        if r.status_code != 200:
            raise IOError('Status code error: code = {}'.format(str(r.status_code)))
        else:
            print('Data has been posted')
    except Exception as e:
        print('Fail to post the data, exception as:')
        print(e)


df_to_update = pd.read_csv('temp.csv')
for i in range(len(df_to_update)):
    curr_df = df_to_update.iloc[i]
    curr_data = json.loads(curr_df.to_json())
    post_daily_product_performance_data(curr_data, to_localhost=False)


