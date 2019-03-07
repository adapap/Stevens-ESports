import flask
from flask import Blueprint

import app.data as data

bp = Blueprint('main', __name__, template_folder='templates')

@bp.route('/')
def index():
    """The homepage for the website."""
    return flask.render_template('index.pug')

@bp.route('/news')
def news():
    """News pertaining to Stevens Esports."""
    games = data.get_games()
    return flask.render_template('news.pug', games=games)

@bp.route('/rosters')
def rosters():
    """Listing of all Stevens Esports teams."""
    games = data.get_games()
    return flask.render_template('rosters.pug', games=games)