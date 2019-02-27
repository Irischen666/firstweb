from . import admin_bp
from flask import render_template, request,redirect, url_for ,jsonify,flash
import pymysql
import json
import time,datetime
from db import MySQL

@admin_bp.route('/',methods=['GET']) # 处理访问请求
def hello_world():
    FIRST_NAME = request.form.get('name')
    MySQL.db_init("127.0.0.1","root","123456")
    dbname="TESTDB"
    param=FIRST_NAME
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
          LAST_NAME, AGE, SEX, INCOME)
          VALUES (%s, 'Mohan', 20, 'M', 2000)"""
    MySQL.db_exesql(dbname,sql,param)
    return jsonify(FIRST_NAME)

@admin_bp.route('/getf', methods=['get'])
def landpage1():
    dbname="TESTDB"
    MySQL.db_init("127.0.0.1","root","123456")
    sql="SELECT FIRST_NAME,LAST_NAME from EMPLOYEE"
    data=MySQL.db_selectone(dbname,sql)
    print(data)
    headers = {'Content-Type': 'application/json'}    ## headers中添加上content-type这个参数，指定为json格式
   # response = request.post(url='url', headers=headers, data=json.dumps(data))    ## post的时候，将data字典形式的参数用json包转换成json格式。
    return jsonify({data})

#下一步数据库拿数据验证登录 
#登录
@admin_bp.route('/login',methods=['GET'])
def login2():
    return render_template('login.html', title="",data={"username":"","password":""})

@admin_bp.route('/login',methods=['POST'])
def login1():
    
    data = request.get_data()
    jsondata = json.loads(data)  #将json字符串解码为python对象
    username = jsondata['username']
    password = jsondata['password']
    code=1;
    try:
        dbname="TESTDB"
        MySQL.db_init("127.0.0.1","root","123456")
        sql = "SELECT * from register where name = %s and pwd = %s "
        param = (username,password)
        results=MySQL.db_findall(dbname,sql,param)
        print (results)
        if len(results)>0:
            code = 0;                  
        else:
            code = 1;
    except Exception as e:
        print("has Error: ",e)
    return jsonify({"code":code,"data":username})  


#注册功能
@admin_bp.route('/register', methods = ['GET'])
def signup():
    return render_template('register.html',title="注册")

@admin_bp.route('/register', methods = ['POST'])
def signup1():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password,type(username))
    db = pymysql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "123456",
        database = "TESTDB",
        charset = 'utf8',
        )
    cursor = db.cursor()
    sql = "SELECT * from register where name = %s" 
    code = 1
    try:
        # 执行SQL语句
        cursor.execute(sql,username)
        results = cursor.fetchall()
        print (results)
        if len(results)>0:   #已经存在
            code = 0
        else:
            code = 1 
            sql = "INSERT INTO register(name,pwd) VALUE(%s,%s)"
            cursor.execute(sql,(username,password))
            db.commit();
    except Exception as e:
        print("has Error: ",e)
        return render_template("error_page.html",error=e)
    db.close();
    return jsonify({"code":code,"username":username})


#留言板功能
@admin_bp.route('/liuyan',methods=['GET'])
def liuyan():
    db = pymysql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "123456",
        database = "TESTDB",
        charset = 'utf8',
        cursorclass= pymysql.cursors.DictCursor
        )
    cursor = db.cursor()
    sql = "SELECT name,comment,create_at from liuyanbd"
    cursor.execute(sql)
    results = cursor.fetchall()    #字典的数组
    db.close();
    print(results)
    greeting_list=jsonify(results)
    return render_template('liuyan.html',greeting_list=results)

@admin_bp.route('/liuyan',methods=['POST'])
def liuyan1():
    name = request.form.get("name",type=str,default=None)
    comment = request.form.get("comment",type=str,default=None)
    # 格式化成2016-03-20 11:45:39形式 
    dt=datetime.datetime.now()
    create_at=dt.strftime('%Y-%m-%d %H:%M:%S')
    print(name,comment,create_at,type(create_at))
    db = pymysql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "123456",
        database = "TESTDB",
        charset = 'utf8',
        cursorclass= pymysql.cursors.DictCursor
        )
    cursor = db.cursor()
    sql = "INSERT INTO liuyanbd(name,comment,create_at)  VALUES (%s, %s,%s) "
    print(1)
    try:
        # 执行sql语句
        cursor.execute(sql,(name,comment,create_at))
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    
    sql = "SELECT name,comment,create_at from liuyanbd"
    cursor.execute(sql)
    results = cursor.fetchall() 
    db.close()
    print(results)
    greeting_list=jsonify(results)
    return render_template('liuyan.html', greeting_list=results)

@admin_bp.route('/vd',methods=['POST'])
def vd():
    name = request.form.get("name")
    comment = request.form.get("comment")
    dt=datetime.datetime.now()
    create_at=dt.strftime('%Y-%m-%d %H:%M:%S')

    #验证name 是否为空，是否是字符串
    msg =""
    vdname =0  #只有同时为非空且为字符串时，vdname=1
    if name:
        if isinstance('name', str) == True:
            vdname=1
        else:
           msg = "数据类型有误"
           return jsonify({"msg":msg})
    else:
        msg = "名字不能为空"
        return jsonify({"msg":msg})
    print(vdname)

    #为字符串则 vdct = 0 ,不为空则 vdct=1  
    vdct = 0 
    if comment:
        if isinstance('comment', str) == True:
            vdct = 1
        else:
            msg = "数据类型有误"
            return jsonify({"msg":msg})
    else:
        msg = "comment can not be null"
        return jsonify({"msg":msg})
    print (vdct)

    while vdname==1 & vdct==1:
        db = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = "123456",
            database = "TESTDB",
            charset = 'utf8',
            cursorclass= pymysql.cursors.DictCursor
            )
        cursor = db.cursor()
        sql = "INSERT INTO liuyanbd(name,comment,create_at)  VALUES (%s, %s,%s) "
        try:
            # 执行sql语句
            cursor.execute(sql,(name,comment,create_at))
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        
        # sql = "SELECT name,comment,create_at from liuyanbd"
        # cursor.execute(sql)
        # results = cursor.fetchall() 
        db.close()
        # print(results)
        print(vdname,vdct)
        msg = "发布成功"
        break;
    return jsonify({"msg":msg})