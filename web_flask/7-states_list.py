#!/usr/bin/python3
"""Flask app to generate html list of all states from storage"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """ Close storage after each request """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ Return a page of alphabetically ordered states """
    from flask import render_template 
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
