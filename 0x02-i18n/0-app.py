#!/usr/bin/env python3
"""The module defines a flask web app"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def hello():
    """renders an html page on screen for path /"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
