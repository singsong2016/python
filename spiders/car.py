
#爬取汽车之家所有车型数据
from bs4 import BeautifulSoup
import requests

html='https://www.autohome.com.cn/grade/carhtml/'


doc=open('out.txt','w')
for i in range(97,97+27):
    url=html+chr(i)+'.html'
    i+=1
    r=requests.get(url)
    r.encoding='gbk'
    soup=BeautifulSoup(r.text,'html.parser')
    zzr=soup.find_all('h4')
    for a in zzr:
       print(a.text,file=doc)
doc.close
