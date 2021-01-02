import os

from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    """GET /"""
    return 'Hello World!'


@app.route('/<name>')
def hello_name(name):
    """GET /<name>"""
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run()
