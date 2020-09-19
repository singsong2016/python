#coding=utf-8

import requests
from bs4 import BeautifulSoup
import string

url = 'http://dy.dsqndh.com/movie.php?m=http://www.360kan.com/dianying/list.php?cat=103%26pageno='



#首先得到每一页的数据，再得到每页30个电影的信息，
#最后筛选得分高于8的电影名字和连接
for i in range(11,20):
    href = url+str(i)
    html = requests.get(href)
    html.encoding='utf-8'
    mess = BeautifulSoup(html.text,"html.parser")
    for n in range(0,30):
     m=mess.select('.s1')[n].text
     o=mess.select('.s2')[n].text
     l=mess.select('.js-tongjic')[n]['href']
     if(o>'8'):
       print(m,o,l)
