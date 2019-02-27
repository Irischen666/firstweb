import pymysql
import os,sys
import time 

class MySQL:
   
    global v_ip
    global v_u  
    global v_p 

    def db_init(ip,u,p):
        global v_ip;
        global v_u;
        global v_p;

        v_ip = ip;
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
    def db_exesql(dbname,sql,param):
        db=MySQL.db_opdb(dbname)
        if(db is None):
            return;
        cursor = db.cursor()
        try:
                cursor.execute(sql,param)
                db.commit()
        except Exception as e:
                print("error,%s",e)
                db.rollback();
        
        db.close();

    def db_findall(dbname,sql,param):
        db=MySQL.db_opdb(dbname)
        if(db is None):
            return(());
        cursor=db.cursor()
        results=(());
        try:
            cursor.execute(sql,param)
            results = cursor.fetchall()
        except Exception as e:
            print("Error:%s",e)
        cursor.close();
        db.close();
        return results;

    def db_selectone(dbname,sql):
        db = MySQL.db_opdb(dbname)
        if(db is None):
            return(());
        cursor=db.cursor()
        results=(());
        try:
            cursor.execute(sql)
            results=cursor.fetchone()
        except Exception as e:
            print("Error:%s",e)
        cursor.close();
        db.close();
        return results;
        


