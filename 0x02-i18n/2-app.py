#!/usr/bin/env python3
"""using babel with flask"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union


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


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Gets locale from request object
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """render templates of home"""

    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
