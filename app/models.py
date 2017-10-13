from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
# mysql://用户名：密码@ip地址：端口号/数据库名称
app.config['SQLACHEMY_DATABASE_URL'] = 'mysql://root:0123456@127.0.0.1:3306/movie'
app.config['SQLACHEMY_TRACK_MODIFICATIONS']= True

db = SQLAlchemy(app)

#会员
class User(db.Model):
    __tablename__ = 'user'
    # 会员id
    id = db.Column(db.Integer, primary_key=True)
    # 昵称
    name = db.Column(db.String(100), unique=True)
    # 密码
    pwd = db.Column(db.String(100))
    # 邮箱
    email = db.Column(db.String(100), unique=True)
    # 手机号码
    phone = db.Column(db.String(11), unique=True)
    # 个性简介
    info = db.Column(db.Text)
    # 头像
    face = db.Column(db.String(225), unique=True)
    # 注册时间
    add_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 唯一标识符
    uuid = db.Column(db.String(255), unique=True)
    #会员日志外键关系关联
    userlogs = db.relationship('Userlog', backref='user')

    def __repr__(self):
        return '<User %r>' % self.name


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer, primary_key=True)
    # 会员id
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 登录ip
    ip = db.Column(db.String(100))
    # 登录时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Userlog %r>' % self.id
