from flask import Flask, render_template, url_for, jsonify
import pandas as pd
import json
from sqlalchemy import create_engine


app = Flask(__name__)
# engine = create_engine('sqlite:///data/data_pro.db')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/performance/chuheyihao', methods=['GET'])
def product_performance():
    df1 = {'a': 5, 'b': 7, 'c': 9}
    return jsonify(df1)

