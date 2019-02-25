import json
import flask
from flask import Blueprint

import app.data as data

bp = Blueprint('main', __name__, template_folder='templates')

@bp.route('/')
def index():
    """The homepage for the website."""
    return flask.render_template('index.pug')

@bp.route('/news.html')
def news():
    """News pertaining to Stevens Esports."""
    flask.flash('WIP')
    return flask.redirect(flask.url_for('main.index'))

@bp.route('/rosters.html')
def rosters():
    """Listing of all Stevens Esports teams."""
    with open('app/data/teams.json') as f:
        raw_data = json.load(f)
    games = []
    for game, game_data in sorted(raw_data.items(), key=lambda x: x[1]['name']):
        games.append(data.Game(game_data))
    return flask.render_template('rosters.pug', games=games)