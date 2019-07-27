from flask import Flask, render_template, url_for, jsonify, redirect, g
from flask_sqlalchemy import SQLAlchemy
import psycopg2 as pg2
import json
import random
from sqlalchemy import create_engine
import os
import psycopg2 as pg2


app = Flask(__name__)


