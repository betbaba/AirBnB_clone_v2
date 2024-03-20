#!/usr/bin/python3
"""starts a web flask applicaton """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """start default route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """start /hbnb route """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
