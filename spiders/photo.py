#coding=utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://www.mzitu.com/26685'

html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')

#最大页数在span标签中的第10个
pic_max = soup.find_all('span')[10].text

#找标题
title = soup.find('h2',class_='main-title').text

#输出每个图片页面的地址
for i in range(1,int(pic_max) + 1):
    href = url+'/'+str(i)
    html = requests.get(href)
    mess = BeautifulSoup(html.text,"html.parser")


    #图片地址在img标签alt属性和标题一样的地方
    pic_url = mess.find('img',alt = title)

    html = requests.get(pic_url['src'])

    #获取图片的名字方便命名
    file_name = pic_url['src'].split(r'/')[-1]

    #图片不是文本文件，以二进制格式写入，所以是html.content
    f = open(file_name,'wb')
    f.write(html.content)
    f.close()