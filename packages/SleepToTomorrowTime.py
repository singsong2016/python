import datetime

import time

tomorrow=datetime.date.today()+datetime.timedelta(days=1)

now=datetime.datetime.now()

def WaitToTomorrowHour(hours):
    tomorrowTime=datetime.datetime.strptime(str(tomorrow.year)+'-'+str(tomorrow.month)+'-'+str(tomorrow.day)+' '+ hours,'%Y-%m-%d %H:%M')
    span=tomorrowTime-now
    print(span.seconds ,' to waiting')
    time.sleep(span.seconds)    
