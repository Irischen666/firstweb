import pymysql

import json


# 打开数据库连接
db = pymysql.connect("127.0.0.1","root","123456","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
FIRST_NAME = "asjjkk"
# LAST_NAME = input('请输入姓：')
# AGE = input('请输入年龄：')
# SEX = input('请输入性别：')
# INCOME = input('请输入收入：')
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
        LAST_NAME, AGE, SEX, INCOME)
        VALUES (%s, 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql,[FIRST_NAME])
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()


# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
#     #    这里的\还有 % (1000) 是？


# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#        # 打印结果
#       print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")
 
# # 关闭数据库连接
# db.close()


# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
 
# # 关闭数据库连接
# db.close()

# # SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (17)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
 
# # 关闭连接
# db.close()


# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#        # 打印结果
#       print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")
 
# # 关闭数据库连接
# db.close()



# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
 
# # 关闭数据库连接
# db.close()




 
# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])