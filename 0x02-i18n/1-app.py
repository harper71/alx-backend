#!/usr/bin/env python3
"""using babel with flask"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """this class sets the default locale for the
    application
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """render templates of home"""

    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
