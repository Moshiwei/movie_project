from . import admin
from flask import redirect, render_template, url_for


@admin.route('/')
def index():
    return render_template('admin/index.html')


@admin.route('/login/')
def login():
    return render_template('admin/login.html')


@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))


@admin.route('/admin_add/')
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route('/admin_list/')
def admin_list():
    return render_template('admin/admin_list.html')


@admin.route('/adminloginlog_list/')
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route('/auth_add/')
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route('/auth_list/')
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route('/comment_list/')
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route('/movie_add/')
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route('/movie_list/')
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route('/moviecol_list/')
def moviecol_list():
    return render_template('admin/moviecol_list.html')


@admin.route('/role_add/')
def role_add():
    return render_template('admin/role_add.html')


@admin.route('/role_list/')
def role_list():
    return render_template('admin/role_list.html')


@admin.route('/preview_list/')
def preview():
    return render_template('admin/preview_list.html')


@admin.route('/preview_add/')
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route('/user_list/')
def user_list():
    return render_template('admin/user_list.html')


@admin.route('/user_view/')
def user_view():
    return render_template('admin/user_view.html')


@admin.route('/userloginlog_list/')
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')


@admin.route('/pwd/')
def pwd():
    return render_template('admin/pwd.html')


@admin.route('/tag_add/')
def tag_add():
    return render_template('admin/tag_add.html')


@admin.route('/tag_list/')
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route('/oplog/')
def oplog():
    return render_template('admin/oplog.html')

