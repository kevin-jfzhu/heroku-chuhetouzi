# run server localy

# import variable app from root/app.py file
from root.app import *


if __name__ == '__main__':
    app.debug = True
    app.run()
