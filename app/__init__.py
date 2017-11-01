from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql://用户名：密码@ip地址：端口号/数据库名称
app.config["SQLACHEMY_DATABASE_URL"] = 'mysql://root:0123456@127.0.0.1:3306/movie'
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = True
# CSRF验证
app.config['SECRET_KEY'] = '6a911d01cbb145268c7d0e248fc91880'
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

