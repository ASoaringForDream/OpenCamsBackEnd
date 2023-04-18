from .auth import db as auth
from .manager import db as manager
from .user import db as user

DEFAULT_BLUEPRINT = [auth, manager, user]

def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)