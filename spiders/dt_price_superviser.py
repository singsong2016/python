import ctypes
import  requests
import threading
import json
#设置递归深度为1百万
import sys
sys.setrecursionlimit(1000000) 

def price():
  html='https://a.dragonex.im/market/buy/?symbol_id=104&callback=_jsonptegx7yxgr2a'
  res=requests.get(html)
  r=res.text
  #原网页数据是非标准json文件，需要出去json以外的字符，然后将str转化为json  dict
  js=json.loads(r[18:-1])
  #获取到的买一价格数据
  pri=float(js['data'][0]['price']
  #弹窗条件
  if(pri>6):
      ctypes.windll.user32.MessageBoxA(0,u"hi,price is higher than 6!".encode('gb2312'),u' 信息'.encode('gb2312'),0)
  if(pri<5):
      ctypes.windll.user32.MessageBoxA(0,u"hi,price is less than 5!".encode('gb2312'),u' 信息'.encode('gb2312'),0)
  #定义变量
  global timer

  #60秒调用一次函数
  timer=threading.Timer(60,price())
  #定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名

  timer.start()    #启用定时器


timer=threading.Timer(1,price())

timer.start()
