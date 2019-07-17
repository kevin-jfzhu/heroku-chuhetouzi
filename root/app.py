from flask import Flask, render_template, url_for, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2 as pg2
import json
import random
from sqlalchemy import create_engine


app = Flask(__name__)

URI = 'postgres://iwohtdhwpoltbw:9d89fa1849631e5a2be1adeadb77bfca08299e8ef168f7daf34eabcb771fcf82@ec2-174-129-227-146.compute-1.amazonaws.com:5432/d1f2cf1peoef92'
conn = pg2.connect(URI, sslmode='require')


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
    cur = conn.cursor()
    try:
        tablename = 'product_performance_' + product_name
        cur.execute("SELECT date, unit_value FROM {};".format(tablename))
        results = cur.fetchall()
        return jsonify({'success_code': 1, 'result_data': results})
    except Exception as e:
        cur.execute("rollback")
        return jsonify({'success_code': 0, 'result_data': [str(e)]})


@app.route('/api/v1/performance/<string:product_name>/update', methods=['POST'])
def update_product_performance(product_name):
    print('The user has updated the product: {}'.format(product_name))
    return redirect('/performance/{}'.format(product_name))

