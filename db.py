import pymysql
import os,sys
import time 

class MySQL:
    __db = None
    __config = {
    'host':"127.0.0.1",
    'username':"root",
    'password':"123456",
    'database':"TESTDB",
    'charset' :"utf8",
    }

    #打卡并连接数据库

    def __init__(self):
        self.__connect()

    def __del__(self):
        if(self.__db is not None):
            self.__db.close()

    def __connect(self):
        try:
            if (self.__db == None):
                self.__db = pymysql.connect(
                    host   =self.__config['host'],
                    user   =self.__config['username'],
                    passwd =self.__config['password'],
                    db     =self.__config['database'],
                    charset=self.__config['charset'],

                )
            return self.__db;
        except Exception as e:
            print("dbcreate ",e)
            print("errdb:"+self.__config['charset']);
            return None;

    #执行语句
    def db_exesql(self,sql,param):
        cursor = self.__connect().cursor()
        try:
            count=cursor.execute(sql,param)
            # 提交到数据库执行
            self.__connect().commit()
            return count
        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False

    #查找全部，带参数查询
    def find_all(self,sql,param):
        cursor = self.__connect().cursor()
        try:
            cursor.execute(sql,param)
            data = cursor.fetchall()
            print(data)
            # 提交到数据库执行
            self.__connect().commit()
        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False
        return data

    #获取所以，不带参数查询
    def show_all(self,sql):
        cursor = self.__connect().cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            # 提交到数据库执行
            self.__connect().commit()
            return data;
        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False


    #查找一个
    def db_selectone(self,sql):
        cursor = self.__connect().cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            # 提交到数据库执行
            self.__connect().commit()
            return data;

        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False
        


