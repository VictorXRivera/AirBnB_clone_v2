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


@app.route('/c/<text>', stric_slashes=False)
def c():
    return "C %s" % escape(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
