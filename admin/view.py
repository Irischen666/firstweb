from . import admin_bp
from flask import render_template, request,redirect, url_for ,jsonify,flash
import pymysql
import json
import time,datetime
from db import MySQL
from .login import *  #from 包.文件名 import 类
from .signup import *

@admin_bp.route('/',methods=['GET']) # 处理访问请求
def hello_world():
    FIRST_NAME = request.form.get('name')
    database= MySQL()
    param=FIRST_NAME
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
          LAST_NAME, AGE, SEX, INCOME)
          VALUES (%s, 'Mohan', 20, 'M', 2000)"""
    database.db_exesql(sql,param)
    return jsonify(FIRST_NAME)

@admin_bp.route('/getf', methods=['get'])
def landpage1():
    sql="SELECT FIRST_NAME,LAST_NAME from EMPLOYEE"
    database=MySQL()
    data=database.db_selectone(sql)
    print(data)
    # headers = {'Content-Type': 'application/json'}    ## headers中添加上content-type这个参数，指定为json格式
   # response = request.post(url='url', headers=headers, data=json.dumps(data))    ## post的时候，将data字典形式的参数用json包转换成json格式。
    return jsonify({"Firstname":data[0],"lastname":data[1]})

#下一步数据库拿数据验证登录 
#登录
@admin_bp.route('/login',methods=['GET'])
def login1():
    return render_template('login.html', title="",data={"username":"","password":""})

@admin_bp.route('/login',methods=['POST'])
def login2():
    data = request.get_data()
    jsondata = json.loads(data)    #将json字符串解码为python对象
    loginb=Login()  #创建对象
    return loginb.check_login(jsondata)  
    ##传参数  
    
     

#注册功能
@admin_bp.route('/register', methods = ['GET'])
def signup():
    return render_template('register.html',title="注册")

@admin_bp.route('/register', methods = ['POST'])
def signup1():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password,type(username))
    signup=Signup()
    return signup.register(username,password)

#留言板功能
@admin_bp.route('/liuyan',methods=['GET'])
def liuyan():
    database= MySQL()
    sql = "SELECT name,comment,create_at from liuyanbd"
    results= database.show_all(sql)
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
    database = MySQL()
    sql = "INSERT INTO liuyanbd(name,comment,create_at)  VALUES (%s, %s,%s) "
    param=(name,comment,create_at)
    results=database.db_exesql(sql,param)
    sql = "SELECT name,comment,create_at from liuyanbd"
    results=database.show_all(sql)
    print(results)
    greeting_list=jsonify(results)
    return render_template('liuyan.html', greeting_list=results)

@admin_bp.route('/vd',methods=['POST'])
def vd():
    name = request.form.get("name")
    comment = request.form.get("comment")
    dt=datetime.datetime.now()
    create_at=dt.strftime('%Y-%m-%d %H:%M:%S')
    print(name,comment,create_at)
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
        database = MySQL()
        param=(name,comment,create_at)
        sql = "INSERT INTO liuyanbd(name,comment,create_at)  VALUES (%s, %s,%s) "
        results=database.db_exesql(sql,param)
        print(vdname,vdct)
        print(results)
        msg = "发布成功"
        break;
    return jsonify({"msg":msg})