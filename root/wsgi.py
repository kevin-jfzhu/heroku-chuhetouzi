# production server deployment

from whitenoise import WhiteNoise

# import Flask instance variable from root/app.py file
from root.app import app

# create decorator for Flask instance
application = WhiteNoise(app)