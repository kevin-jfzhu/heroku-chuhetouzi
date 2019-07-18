from flask import Flask, render_template, url_for, jsonify, redirect
import pandas as pd
import json
import random
from sqlalchemy import create_engine
import os
import psycopg2 as pg2


app = Flask(__name__)

# DATABASE_URL = os.environ.get('database_url')
conn = pg2.connect(DATABASE_URL, sslmode='require')

"""---------------------------------  Pages & Router Definition ---------------------------------"""


# @app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
@app.route('/dashboard.html', methods=['GET'])
def dashbaord():
    return render_template('dashboard.html')


@app.route('/register', methods=['GET'])
@app.route('/register.html', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/forgot-password', methods=['GET'])
@app.route('/forgot-password.html', methods=['GET'])
def forgot_password():
    return render_template('forgot-password.html')


@app.route('/login', methods=['GET'])
@app.route('/login.html', methods=['GET'])
def login():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/products', methods=['GET'])
@app.route('/products.html', methods=['GET'])
def products():
    return render_template('products.html')


@app.route('/strategies', methods=['GET'])
@app.route('/strategies.html', methods=['GET'])
def strategies():
    return render_template('strategies.html')


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
            dates.append(row[0])
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
    return redirect('/performance/{}'.format(product_name))

