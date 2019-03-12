import pymysql
import os,sys
import time 
import json
from flask import render_template, request,redirect, url_for ,jsonify,flash
from db import MySQL


class Login:
    def __init__(self):
        self.get_loginpage()

    def get_loginpage(self):
        return render_template('login.html', title="",data={"username":"","password":""})

    def check_login(self):
        data = self.request.get_data()
        jsondata = self.json.loads(data)  #将json字符串解码为python对象
        username = self.jsondata['username']
        password = self.jsondata['password']
        print(username,password)
        code=1;
        database=self.MySQL()
        try:
            sql = "SELECT * from register where name = %s and pwd = %s "
            param = (username,password)
            results = database.db_exesql(sql,param)
            print (results)
            if len(results)>0:
                code = 0;                  
            else:
                code = 1;
        except Exception as e:
            print("has Error: ",e)
        return jsonify({"code":code,"data":username})  
