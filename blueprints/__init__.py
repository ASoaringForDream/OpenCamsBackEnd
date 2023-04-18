from .auth import db as auth
from .manager import db as manager

DEFAULT_BLUEPRINT = [auth, manager]

def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)