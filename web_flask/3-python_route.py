#!/usr/bin/python3
""" Making a Flask script """
from flask import Flask, escape, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python/(<text>)', strict_slashes=False)
def python_route(text):
    text = text.replace('_', ' ')
    return "Python %s" % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
