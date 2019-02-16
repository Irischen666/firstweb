from . import admin_bp
from flask import render_template
import pymysql
from flask import request,redirect, url_for ,jsonify
import json
# from flask import current_app as app

#  蓝图对象 admin_bp 注册访问地址 如下：
#  http://127.0.0.1:5000/admin/
@admin_bp.route('/',methods=['GET']) # 处理访问请求
# def index():
#     return '<h1>Hello, this is admin blueprint</h1>'
def hello_world():
    
    db = pymysql.connect("127.0.0.1","root","123456","TESTDB" )
    cursor = db.cursor()
    FIRST_NAME = request.args.get("name")
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
          LAST_NAME, AGE, SEX, INCOME)
          VALUES (%s, 'Mohan', 20, 'M', 2000)"""
    try:
        # 执行sql语句
        cursor.execute(sql,FIRST_NAME)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    return FIRST_NAME


@admin_bp.route('/register', methods=['POST'])
def register():

    name=request.form["username"];
    pwd = request.form["password"];


    db = pymysql.connect("127.0.0.1","root","123456","TESTDB" )
    cursor = db.cursor()
    sql = """INSERT INTO register(name, pwd) VALUES (%s,%s)"""
    try:
        cursor.execute(sql,(name,pwd))
        db.commit()
    except Exception as e:
        db.rollback()
        return "err:"+ str(e)
    db.close()
    return 'you name : %s you pwd %s' %(name,pwd)



#   蓝图对象 admin_bp 注册访问地址 如下：
#   http://127.0.0.1:5000/admin/hello
@admin_bp.route('/hello',methods=['GET']) # 处理访问请求
def index2():
    return '<h1>Say ! Hello</h1>'


@admin_bp.route("/a",methods=['GET'])
def a():
    user = {'nickname': 'Miguel'}
    xx={"xx":"xx is not any way"}
    return render_template("index.html",myusery=user,xx=xx)
    # return "<html><head><title>TTTT</title></head><body><h1>my name is ...</h1></body></html>"
    #作业：数据库操作
    


@admin_bp.route("/db",methods=['POST','GET'])
def create_table():
    # 1. 链接数据库
    # db = pymysql.connect("127.0.0.1","root","123456","TESTDB" )
    # #使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # # 使用 execute()  方法执行 SQL 查询 
    # cursor.execute("SELECT VERSION()")
    
    # # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    
    # print ("Database version : %s " % data)
    
    # # 关闭数据库连接
    # db.close()


    # #2. 创建数据库表格
    # db = pymysql.connect("127.0.0.1","root","123456","TESTDB" )
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    
    # # 使用 execute() 方法执行 SQL，如果表存在则删除
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    
    # # 使用预处理语句创建表
    # sql = """CREATE TABLE EMPLOYEE (
    #         FIRST_NAME  CHAR(20) NOT NULL,
    #         LAST_NAME  CHAR(20),
    #         AGE INT,  
    #         SEX CHAR(1),
    #         INCOME FLOAT )"""
    
    # cursor.execute(sql)

    # # 关闭数据库连接
    # db.close()

    # 3.插入数据

    xxx=request.args.get('abc')
    print("xxx",xxx)






    # # 打开数据库连接
    # db = pymysql.connect("127.0.0.1","root","123456","TESTDB" )
    
    # # 使用cursor()方法获取操作游标 
    # cursor = db.cursor()
    
    # # SQL 插入语句
    # FIRST_NAME = "abbdd"
    # # LAST_NAME = input('请输入姓：')
    # # AGE = input('请输入年龄：')
    # # SEX = input('请输入性别：')
    # # INCOME = input('请输入收入：')
    # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    #         LAST_NAME, AGE, SEX, INCOME)
    #         VALUES (?, 'abc', 21, 'M', 3000)"""
    # try:
    #     # 执行sql语句
    #     cursor.execute(sql,[FIRST_NAME])
    #     # 提交到数据库执行
    #     db.commit()
    # except:
    #     # 如果发生错误则回滚
    #     db.rollback()
    
    # # 关闭数据库连接
    # db.close()



@admin_bp.route('/postf', methods=['POST'])
def landpage():
    data = {
        'time': 'Miguel',
        "title":"first title"
    }
    
    headers = {'Content-Type': 'application/json'}    ## headers中添加上content-type这个参数，指定为json格式
    response = request.post(url='url', headers=headers, data=json.dumps(data))    ## post的时候，将data字典形式的参数用json包转换成json格式。
    return render_template("index.html",time=data.time,title=data.title)

@admin_bp.route('/getf', methods=['get'])
def landpage1():
   
    db = pymysql.connect("127.0.0.1","root","123456","TESTDB" )
    #使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT FIRST_NAME,LAST_NAME from EMPLOYEE")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    # 关闭数据库连接
    cursor.close()
    db.close()
    #data=json.dumps(data)
    print (data)
    headers = {'Content-Type': 'application/json'}    ## headers中添加上content-type这个参数，指定为json格式
   # response = request.post(url='url', headers=headers, data=json.dumps(data))    ## post的时候，将data字典形式的参数用json包转换成json格式。
    return render_template("index.html",title="----test----",time=data)

@admin_bp.route('/login',methods=['GET','POST'])  #一般情况要get post 方法分开写
# def login():
#     error = None
#     if request.method == 'POST':
        
#         if request.post['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect('admin/hello')
#     return render_template('login.html', error=error)

def login1():
    if request.method == 'POST':
        data = request.get_data()   #字符串
        print("etdata----",data)
        jsondata=json.loads(data)   #字符串转化成对象  一般字典类型，哈希表，map json解析成字典类型 key:value
        username = jsondata['username']
        password = jsondata['password']
        return jsonify({"logignname": "username","logignpwd": "password"})  #对象再转换成字符串
    return render_template('login.html', title="",data={"username":"","password":""})

#下一步数据库拿数据验证登录 