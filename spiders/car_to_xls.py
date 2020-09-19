
#一般性约定：x表示变量，后面的数字表示第几个，最后一个后面不带数字,要使用本程序需要将变量更改为具体内容


from bs4 import BeautifulSoup
import requests

from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('test.xls')                   #x1_filename.xls 需要写入本地的xls文件名，不支持xlsx
#通过sheet_by_index()获取的sheet没有write()方法
rs = rb.sheet_by_index(0)

wb = copy(rb)
#通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)

#写入表格第几行的参数l
l=3
column=0
#根网址
html='https://www.autohome.com.cn/spec/'       #x2_root_url

#由于数据量太大，为了效率仅爬取50个车子数据，更改一下数字可以调整获取到的数据条数
for b in range (1002000,1002050):            #x3_start_page,x4_end_page
  url=html+str(b)+'/'
  r=requests.get(url)
  r.encoding='gbk'
  soup=BeautifulSoup(r.text,'html.parser')



    #如果页面存在，则保存数据
  if(r.status_code==200 ):               #x5_status_code

      ws.write(l, column, soup.select('a')[71].text+soup.select('a')[72].text)    #x6_tag,x7_number

      v=soup.find_all('li',class_='cardetail-right')                            #x8_tag,x9_classname
      if(len(v[0].text)>22):
         ws.write(l, column+1, '暂无')
      else:
         ws.write(l, column+1, v[0].text)

#质保
      ws.write(l, column+2, soup.select('li')[57].text)

      ws.write(l, column+3, 1)
      ws.write(l, column+4, url)
#价格
      z=soup.find_all('span',attrs={'data-price':True})                    #x10_attris
      ws.write(l, column+5, z[0]['data-price'])

#二手车参考价
      y=soup.find_all('div',class_='fn-left ml10')
      if(len(y)>1):
        ws.write(l, column+6, y[1].text)
      else:
        ws.write(l, column+6, '暂无')

      ws.write(l, column+7, soup.select('li')[60].text)

      o=soup.find_all('a',class_='fn-fontsize14 font-bold')
      if(len(o)>0):
         ws.write(l, column+8, o[0].text)
      else:
          ws.write(l, column+8, '暂无')
      l+=1


wb.save('test.xls')
