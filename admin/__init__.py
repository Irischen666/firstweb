from flask import Blueprint

print("---->"+__name__);
admin_bp = Blueprint('admin', __name__) #生成蓝图对象

from . import  view
from . import login