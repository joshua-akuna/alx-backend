#!/usr/bin/env python3
"""The module defines a flask web app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """configuration for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask("__name__")
app.config.from_object(Config)
babel = Babel()


@app.route("/", strict_slashes=False)
def hello():
    """renders an html page on screen for path /"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
