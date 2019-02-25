import logging
from flask import Flask
from flask_scss import Scss

from app.routes import bp

def create_app():
    """App creating factory for deployment."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = r'-\x0c(q\xe0#/\xd4\x9c\x1d\x99\xa2\x16f[\x9b'

    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True
    app.register_blueprint(bp)

    # Pug - HTML Template Engine
    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
    # Sass - CSS Preprocessor
    Scss(app, static_dir='app/static/css', asset_dir='app/static/scss')
    
    return app