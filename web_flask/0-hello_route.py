#!/usr/bin/python3
""" Making a Flask script """

from flask import Flask, escape, request
app = Flask(__name__)

@app.route('/')
def hello_HBNB():
	strict_slashes=False
	return 'Hello HBNB!'
