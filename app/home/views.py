from . import home
from flask import render_template, redirect, url_for


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/login/')
def login():
    return render_template('home/login.html')


@home.route('/logout/')
def logout():
    return redirect(url_for('home.login'))


@home.route('/register/')
def register():
    return render_template('home/register.html')


@home.route('/user/')
def user():
    return render_template('home/user.html')


@home.route('/user/pwd/')
def pwd():
    return render_template('home/pwd.html')

@home.route('/user/comments/')
def comments():
    return render_template('home/comments.html')

@home.route('/user/loginlog/')
def loginlog():
    return render_template('home/loginlog.html')

@home.route('/user/moviecol/')
def moviecol():
    return render_template('home/moviecol.html')

@home.route('/animation/')
def animation():
    return render_template('home/animation.html')

@home.route('/search/')
def search():
    return render_template('home/search.html')