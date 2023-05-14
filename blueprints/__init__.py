from .auth import db as auth
from .manager import db as manager
from .user import db as user
from .role import db as role
from .cam import db as cam

DEFAULT_BLUEPRINT = [auth, manager, user, role, cam]

def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)