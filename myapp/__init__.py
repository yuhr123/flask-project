from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return 'Hello world!'

# Blueprint
from .views import user

app.register_blueprint(user.mod)