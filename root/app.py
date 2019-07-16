from flask import Flask, render_template, url_for, jsonify
import pandas as pd
import json
import random
from sqlalchemy import create_engine


app = Flask(__name__)
# engine = create_engine('sqlite:///data/data_pro.db')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
@app.route('/login.html', methods=['GET'])
def login():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/blank', methods=['GET'])
@app.route('/blank.html', methods=['GET'])
def blank():
    return render_template('blank.html')


@app.route('/charts', methods=['GET'])
@app.route('/charts.html', methods=['GET'])
def charts():
    return render_template('charts.html')


@app.route('/tables', methods=['GET'])
@app.route('/tables.html', methods=['GET'])
def tables():
    return render_template('tables.html')


@app.route('/performance/chuheyihao', methods=['GET'])
def product_performance():
    df1 = [random.randint(1, 10) for x in range(6)]
    return jsonify(df1)

