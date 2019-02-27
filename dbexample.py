#!/usr/bin/python3

import pymysql
import os, sys
import time

#初始化数据#生产 sql 批量插入文件
# #
global v_ip
global v_u
global v_p

# v_ip="111"
# v_u=""
# v_p=""

def db_init(ip,u,p):
    global v_ip;
    global v_u;
    global v_p;
    v_ip=ip;  #数据库的IP 用户名 密码
    v_u=u;
    v_p=p;

#打开数据库
def db_opdb(dbname):
    global v_ip;
    global v_u;
    global v_p;
    # 打开数据库连接
    try:
            # print("%s,%s,%s" % (v_ip,v_u,v_p));
            db = pymysql.connect(v_ip,v_u,v_p,dbname)
            return db;
    except Exception as e:
            print("dbcreate ",e)
            print("errdb:"+dbname);
    return None;

#执行语句
def db_exesql(dbname,sql):
      db=db_opdb(dbname)
      if(db is None):
        return;
      cursor = db.cursor()
      try:
            cursor.execute(sql)
            db.commit()
      except Exception as e:
            print("error,%s",e)
            db.rollback();
      
      db.close();

#查询语句
def db_selectsql(dbname,sql):
      db=db_opdb(dbname)
      if(db is None):
            return (());
      cursor = db.cursor()
      results=(());
      try:
            # 执行SQL语句
            cursor.execute(sql)
            # db.commit();
            # 获取所有记录列表
            results = cursor.fetchall()
            # for row in results:
            #       uid = row[0]
            #       userid = row[1]
            #       username = row[2]
            #       phone = row[3]
            #       email = row[4]
            #       # 打印结果
            #       print("uid=%s,userid=%s,username=%s,phone=%s",uid,userid,username,phone)
                  #return userid;
      except Exception as e:
            print("Error: %s",e)
      
      # print("result:--%s",results)
      cursor.close();
      db.close();
      # print("result2:--%s",results)
      return results;

#查询是否存在(select count(1) from xxx )
def db_has(dbname,sql):
      db=db_opdb(dbname)

      cursor = db.cursor()
      last=False;
      try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                  uid = row[0]
                  if uid>0:
                         last = True;
                         break;
      except Exception as e:
            print("has Error: %s",e)
      db.close();

      return last;

def db_testOut():
    global v_ip;
    global v_u;
    global v_p;
    print("ip %s",v_ip)
    print("v_u %s",v_u)
    print("v_p %s",v_p)