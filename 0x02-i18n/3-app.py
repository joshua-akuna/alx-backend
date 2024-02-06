#!/usr/bin/env python3
"""The module defines a flask web app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask("__name__")
app.config.from_object(Config)
babel = Babel()


@babel.localeselector
def get_locale():
    """Uses the request.accept_languages to determine
        the best match with the supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def hello():
    """renders an html page on screen for path /"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
