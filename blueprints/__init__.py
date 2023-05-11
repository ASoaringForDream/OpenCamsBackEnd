from .auth import db as auth
from .manager import db as manager
from .user import db as user
from .role import db as role

DEFAULT_BLUEPRINT = [auth, manager, user, role]

def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)