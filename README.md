# Flask Heroku Example


This repo contains some sample code to deploy a simple Flask application to [Heroku](https://heroku.com). The deployed app counts with the following features:

* Running Python 3.7 🐍
* Static Files management with [WhiteNoise](http://whitenoise.evans.io/en/stable/) 🔌

## Summary of steps to deploy your app
_(Assuming you've already created an account with Heroku)_

##### 1. Clone the repo
```bash
$ git clone https://github.com/igortereshchenko/flask_heroku_template.git && cd flask-heroku-example
```

##### 2. Login to Heroku
```bash
$ heroku login
```

##### 3. Create your Heroku apps
```bash
$ heroku create
```

##### 4. Set the Python Path
```bash
$ heroku config:set PYTHONPATH=flask_heroku_template
```

##### 5. Deploy & Profit
```bash
$ git push heroku master
```

##### 6. Open and enjoy
```bash
$ heroku open
```

based on work of https://github.com/rmotr-curriculum