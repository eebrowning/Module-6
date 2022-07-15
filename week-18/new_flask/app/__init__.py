from flask import Flask
from app.config import Config
app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SECRET_KEY'])


@app.route('/')
def index():
    print('youre in the route')
    return "<h1>Welcome!</h1>"
