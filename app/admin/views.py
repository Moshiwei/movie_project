from . import admin
from flask import redirect, render_template, url_for

@admin.route('/')
def index():
    return "<h1 style='color:green'>this is admin</h1>"

@admin.route('/login/')
def login():
    return render_template('admin/login.html')

@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))