from flask import Flask
from flask import request
from flask import abort, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('hello'))


@app.route('/hello', methods=["GET"])
def hello():
    if request.method == "GET":
        return "<H1>Hello<H1>"


if __name__ == '__main__':
    app.run()
