from . import admin

@admin.route('/')
def index():
    return "<h1 style='color:green'>this is admin</h1>"