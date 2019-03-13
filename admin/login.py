import pymysql
import os,sys
import time 
import json
from flask import render_template, request,redirect, url_for ,jsonify,flash
from db import MySQL


class Login:
    def __init__(self):
        # self.check_login()
        pass
    def check_login(self,jsondata):   #成员变量和局部变量,self 只能.调用成员变量，不能jsondata 是方法内使用，使用结束后就删除了
        username = jsondata['username']
        password = jsondata['password']
        print(username,password)
        code=1;
        database=MySQL()
        try:
            sql = "SELECT * from register where name = %s and pwd = %s "
            param = (username,password)
            results = database.db_exesql(sql,param)
            # print(results)
            # print (type(results))
            if results>0:
                code = 0;                
            else:
                code = 1;
        except Exception as e:
            print("has Error: ",e)
        # print(code)
        r={"code":code,"data":username}
        return jsonify(r)
