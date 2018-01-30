from flask import Blueprint, render_template
from ..database import db_session, User

mod = Blueprint('user', __name__, url_prefix='/user/')

# 常规示例，访问 http://localhost:5000/user/
@mod.route('/')
def index():
    return '这是 user 蓝图下的页面'

# 渲染模板示例，访问 http://localhost:5000/user/tpl/
@mod.route('tpl/')
def tpl():
    data = {
        'title': 'Blueprint 模板样例',
        'content': '这里是一些传入模板的样例文本',
    }
    return render_template('user/example.html', data=data)

@mod.route('data/')
def show():
    data = {
        'title': '读取数据示例',
        'user': User.query.get(1),
        'list': User.query.all(),
    }
    return render_template('user/show.html', data=data)