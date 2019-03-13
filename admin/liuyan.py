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