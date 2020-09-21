import packages.mailT as sm
import packages.sleepToTomorrow as slp
import requests

# this pattern monitor any kind of financial price 
# to inform by mail
url='http://hq.sinajs.cn/list=gds_AUTD'

while True:  
    slp.WaitToTomorrowHour('14:00')    
    s=requests.get(url)
    price=float(s.text[21:27])
    if price<400:
        sm.sendmail('gold price','au9999 is under 400')