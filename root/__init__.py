from flask import Flask, render_template, url_for, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2 as pg2
import json
import random
from sqlalchemy import create_engine
import os
import psycopg2 as pg2


app = Flask(__name__)
conn = pg2.connect(os.environ.get('HEROKU_DB_URL'), sslmode='require')
