# creating Flask instance variable app

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'it works!'


@app.route('/<name>')
def hello(name):
    return 'it works! {0}'.format(name)