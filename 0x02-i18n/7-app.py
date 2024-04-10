#!/usr/bin/env python3
"""Infer appropriate time zone"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user information"""
    user_id = request.args.get('login_as', type=int)
    if user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """Set user as global"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Get locale"""
    if 'locale' in request.args:
        return request.args['locale']
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Get time zone"""
    if 'timezone' in request.args:
        try:
            return pytz.timezone(request.args['timezone'])
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone'] in pytz.all_timezones:
        return pytz.timezone(g.user['timezone'])
    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


@app.route('/')
def index():
    """Route for home page"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
