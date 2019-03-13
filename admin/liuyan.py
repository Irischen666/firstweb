import pymysql
import os,sys
import time 
import json
from flask import render_template, request,redirect, url_for ,jsonify,flash
from db import MySQL

class Liuyan:
    def __init__(self):
        pass

    def find_liuyan(self):
        database= MySQL()
        sql = "SELECT name,comment,create_at from liuyanbd"
        results= database.show_all(sql)
        # print(results)
        return results
    
    def add_liuyan(self,name,comment,create_at):
        database = MySQL()
        sql = "INSERT INTO liuyanbd(name,comment,create_at)  VALUES (%s, %s,%s) "
        param=(name,comment,create_at)
        results=database.db_exesql(sql,param)
        sql = "SELECT name,comment,create_at from liuyanbd"
        results= database.show_all(sql)
        # print(results)
        return results