import pymysql
import os,sys
import time 
import json
from flask import render_template, request,redirect, url_for ,jsonify,flash
from db import MySQL

class Signup:
    def __init__(self):
        pass
    def register(self,username,password):
        code = 1
        database=MySQL()
        param = (username,password)
        print(param[0])
        try:
            # 执行SQL语句
            sql = "SELECT * from register where name = %s" 
            results = database.find_all(sql,param[0])
            print (results)
            if len(results)>0:   #已经存在
                code = 0
            else:
                code = 1 
                sql = "INSERT INTO register(name,pwd) VALUE(%s,%s)"
                results=database.db_exesql(sql,param)
        except Exception as e:
            print("has Error: ",e)
            return render_template("error_page.html",error=e)
        return jsonify({"code":code,"username":param[0]})
