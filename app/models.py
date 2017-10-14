from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
# mysql://用户名：密码@ip地址：端口号/数据库名称
app.config['SQLACHEMY_DATABASE_URL'] = 'mysql://root:0123456@127.0.0.1:3306/movie'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# 会员
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)  # 会员id
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(225), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关系关联

    def __repr__(self):
        return '<User %r>' % self.name  # 会员登录日志


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 会员id
    ip = db.Column(db.String(100))  # 登录ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 登录时间

    def __repr__(self):
        return '<Userlog %r>' % self.id


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    movies = db.relationship('Movie', backref='tag')  # 电影外键关系关联

    def __repr__(self):
        return '<Tag %r>' % self.name


# 电影
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    info = db.Column(db.Text)  # 简介
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    area = db.Column(db.String(255))  # 地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时长
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签

    def __repr__(self):
        return '<Movie %r>' % self.title

# 上映预告
class Preview(db.Model):
    __tablename__ = 'Preview'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)  # 标题
    # url = db.Column(db.String(255), unique=True)  # 地址
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return '<Preview %r>' % self.title