import pytz
import time
import datetime

def getweekdaybytz(timezone):
    tz = pytz.timezone(timezone)
    t = time.time()
    dt1 = datetime.datetime.fromtimestamp(t)
    dt2=  dt1.astimezone(tz)
    return dt2.weekday()

def getdatestrbytzfortrvtime(timezone):
    tz = pytz.timezone(timezone)
    t = time.time()
    dt1 = datetime.datetime.fromtimestamp(t)
    dt2=  dt1.astimezone(tz)
    return dt2.strftime('%a%H%M')

def getdatestrbytz(timezone):
    tz = pytz.timezone(timezone)
    t = time.time()
    dt1 = datetime.datetime.fromtimestamp(t)
    dt2=  dt1.astimezone(tz)
    return dt2.strftime('%Y-%m-%d %H:%M:%S')

def withinstrend(strtime,endtime,lang):
    tz = pytz.timezone(lang)
    t = time.time()
    dt1 = datetime.datetime.fromtimestamp(t)
    dt2=  dt1.astimezone(tz)
    dt3 = datetime.datetime.time(dt2)
    curdelta = datetime.timedelta(hours=dt3.hour,minutes=dt3.minute,seconds=dt3.second)
    res1 = True
    if (not strtime<curdelta<endtime) and (strtime != endtime):
        res1 = False
    elif strtime>endtime and (strtime> curdelta >endtime) :
        res1 = False
    res2 = False
    if strtime<endtime and endtime< curdelta:
        res2 = True
    return [res1,res2]
if __name__ == '__main__':
    #print(getdatestrbytz('US/Eastern'))
    #print(getdatestrbytz('Asia/Taipei'))
    mtime = int(time.time())
    print('mtime',mtime)

#     withinstrend(0,0)
#    print(getweekdaybytz('Asia/Taipei'))
