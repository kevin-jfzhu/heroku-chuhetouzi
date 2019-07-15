from flask import Flask, render_template, url_for, jsonify
import pandas as pd
import json
from sqlalchemy import create_engine


app = Flask(__name__)
engine = create_engine('sqlite:///data/data_pro.db')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    # df = pd.read_sql_table('chuheyihao_performance', con=engine, schema='main')
    # df1 = df[['unit_value', 'unit_value_change']]
    # df1.index = df.date
    return render_template('index.html')


@app.route('/performance/chuheyihao', methods=['GET'])
def product_performance():
    df = pd.read_sql_table('chuheyihao_performance', con=engine, schema='main')
    df1 = df[['unit_value', 'unit_value_change']]
    df1.index = df.date
    return jsonify(json.loads(df1.to_json()))

