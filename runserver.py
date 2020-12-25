#coding=utf-8

from flask import Flask,request
from datetime import datetime
import logging
from commands.defcmd import *
from flask_babel import *
import sys
sys.path.append('config')
from config import *

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
babel = Babel(app)
status_str = ""

def error_log(app,logstr):
    currtimestring = datetime.now().strftime('%Y%m%d %H:%M:%S')
    app.logger.info(currtimestring+' %s'%logstr)

def command1(str):
    str = "%s%s" % (str , 'in command1')
    print(str)
def command2(str):
    str += "%s%s" % (str , 'in command2')
    print(str)

def command3(str):

    str += "%s%s" % (str , DEFAULT_TIMEZONE)
    print(str)

def other(str):
    str += "%s%s" % (str , 'in other')
    print(str)


def switch_cmd(num,str):
    numbers = {
        CMD1: command1,
        CMD2: command2,
        CMD3: command3
    }
    method = numbers.get(num,other)
    if method:
        method(str)

@app.route('/test', methods=['GET'])
def get_test():
    cmdid = request.values.get('id')
    logstr = 'call test get id=> %s'% cmdid
    error_log(app, logstr)
    switch_cmd(int(cmdid), logstr)
    return logstr

if __name__ == '__main__':
    app.debug = True
    log_filename = datetime.now().strftime("log_%Y-%m-%d.log")
    handler = logging.FileHandler(log_filename)
    print("app--------------------")
    app.logger.addHandler(handler)
    error_log(app,'web start ')
    app.run(host='0.0.0.0',port='5000',debug=True)