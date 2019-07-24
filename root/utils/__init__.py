from flask import Flask, render_template, url_for, jsonify, redirect, g
from flask_sqlalchemy import SQLAlchemy
import psycopg2 as pg2
import json
import random
from sqlalchemy import create_engine
import os
import psycopg2 as pg2



app = Flask(__name__)
LOCAL_DB = 'postgresql://kevinzhu:Mcgrady1@127.0.0.1:5432/mydb'
DATABASE_URL = os.environ.get('DATABASE_URL')

