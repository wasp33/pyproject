#coding=utf-8
from flask import Flask,request
from datetime import datetime
import logging
from flask_babel import *


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
babel = Babel(app)

def error_log(app,logstr):
    currtimestring = datetime.now().strftime('%Y%m%d %H:%M:%S')
    app.logger.info(currtimestring+' %s'%logstr)

@app.route('/test')
def get_test():
    error_log(app,'call test')
    return 'OK'

if __name__ == '__main__':
    app.debug = True
    log_filename = datetime.now().strftime("log_%Y-%m-%d.log")
    handler = logging.FileHandler(log_filename)
    print("app--------------------")
    app.logger.addHandler(handler)
    error_log(app,'web start ')
    app.run(host='0.0.0.0',port='5000',debug=True)