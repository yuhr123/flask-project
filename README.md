## 使用方法

* 创建 `venv` 虚拟环境；
* 克隆项目到虚拟环境，将 `myapp` 目录重命名为实际的项目名；
* 将 `setup.py` 中的 `name` 和 `package` 两项修改成实际的项目名；

### 设置应用名称环境变量
```
export FLASK_APP=myapp
```

### 启用调试模式
```
export FLASK_DEBUG=true
```

### 安装项目依赖
```
pip install -e .
```

### 运行程序
```
flask run
```

## 关于数据库

在项目目录下运行 `Python` 交互命令行

导入数据库配置文件：
```
>>> from myapp import database
```

执行数据库初始化：
```
>>> database.init_db()
```

数据库使用 `flask-sqlalchemy` 扩展，使用方法请参考官方文档：http://flask-sqlalchemy.pocoo.org

