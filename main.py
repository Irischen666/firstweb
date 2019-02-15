from flask import Flask

import sys;

from user import abc

from admin import  admin_bp #导入模块

 
app = Flask(__name__)
app.register_blueprint(admin_bp, url_prefix='/admin') #注册模块
 
# print(__name__)
# abc.funac()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


