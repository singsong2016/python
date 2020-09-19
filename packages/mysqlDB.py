#pip3 install pymysql 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","123456","Test" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

def GetData(sql):

    # 使用 execute()  方法执行 SQL 查询 
    # cursor.execute("select * from hello")
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    
    # 关闭数据库连接
    db.close()

    return data
    # print (data)
    

def ExecuteSql(sql):
    try:
       result = cursor.execute(sql)
       db.commit()
    except :
        result='err'
    db.close()
    return result

# call demo 
   # install driver first =>  pip3 install PyMySQL
    # from mysqlDB import GetData,ExecuteSql

    # s='select * from hello'

    # result=GetData(s)

    # for i in result:
    #     print(i)

    # s='insert into hello(name) values("zhou")'

    # result=ExecuteSql(s)

    # print(result)
