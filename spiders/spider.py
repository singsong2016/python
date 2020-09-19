import requests
from bs4 import BeautifulSoup


#get html

res=requests.get('http://news.sina.com.cn/china/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')


#BeautifulSoup

for news in soup.select('.news-item'):    
    if len(news.select('h2'))>0:
        h2=news.select('h2').text
        time=news.select('.time')[0].text
        a=news.select('a')[0]['href']
        print(h2,time,a)
