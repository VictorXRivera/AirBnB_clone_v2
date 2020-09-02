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


@app.route('/python', defaults={'text': None}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text):
    if text is None:
        text = 'is cool'
    text = text.replace('_', ' ')
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_render_template(n):
    """ Number template function """
    from flask import render_template
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    "Odd or even num template"
    from flask import render_template
    if n % 2 == 0:
        oe = 'even'
    else:
        oe = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, oe=oe)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
