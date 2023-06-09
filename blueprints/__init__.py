from .auth import db as auth
from .manager import db as manager
from .user import db as user
from .role import db as role
from .cam import db as cam
from .dashboard import db as dashBorad

DEFAULT_BLUEPRINT = [auth, manager, user, role, cam, dashBorad]

def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)