#!/usr/bin/python3
""" Making a Flask script """

from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        return 'Hello HBNB!'
