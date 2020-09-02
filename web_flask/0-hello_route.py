#!/usr/bin/python3
""" Making a Flask script """

from flask import Flask, escape, request
app = Flask(__name__)
strict_slashes = False


@app.route('/')
def hello_HBNB():
        return 'Hello HBNB!'
