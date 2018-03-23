import os

from flask import Flask
from flask.cli import FlaskGroup, click
from flask_debugtoolbar import DebugToolbarExtension

from sweext.models.models._base import db

from ..exceptions.http_error import HttpError
from ..views import home, steps, claim
from ..views.home.urls import HomeUrlRegister
from ..views.steps.urls import StepsUrlRegister
from ..views.claim.urls import ClaimUrlRegister


def create_app(script_info=None):
    app = Flask('sweext_web', static_url_path='')
    # check the env is prod or dev
    if os.getenv('RUN_IN_PROD') == 'True':
        app.config.from_object('sweext_web.config.web_config.Config')
    else:
        app.config.from_object('sweext_web.config.web_config_dev.DevConfig')

    db.init_app(app)

    HomeUrlRegister.register()
    StepsUrlRegister.register()
    ClaimUrlRegister.register()

    app.register_blueprint(home.views.home_blueprint)
    app.register_blueprint(steps.views.steps_blueprint)
    app.register_blueprint(claim.views.claim_blueprint)

    app.debug = False
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    app.register_error_handler(401, HttpError.handle_401)
    app.register_error_handler(403, HttpError.handle_403)
    app.register_error_handler(404, HttpError.handle_404)
    app.register_error_handler(405, HttpError.handle_405)
    app.register_error_handler(500, HttpError.handle_500)

    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass
