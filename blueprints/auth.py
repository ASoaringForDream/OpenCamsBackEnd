from flask import Blueprint, request, jsonify, session, make_response
from models.manager import Manager
from models.user import User
from models.role import Role, Roleitem

db = Blueprint("auth", __name__, url_prefix='/manager')

@db.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username = data['username']
    password = data['password']
    manager = Manager.query.filter(Manager.username == username).first()
    if manager != None:
        if manager.password != password:
            return jsonify({
                "errno": 1,
                "errmsg": '密码错误'
            })
        else:
            session["username"] = username

            return jsonify({
                "errno": 0,
                "errmsg": '',
            })
    else:
        return jsonify({
            "errno": 1,
            "errmsg": '用户不存在'
        })


@db.route("/session", methods=["POST"])
def check_session():
    user = session.get("username")
    if user:
        manager = Manager.query.filter(Manager.username == user).first()
        return jsonify({
            "errno": 0,
            "errmsg": '',
            "data": manager.to_json()
        })
    else:
        return jsonify({
            "errno": 1,
            "errmsg": '用户未登录',
        })


@db.route("/logout", methods=["DELETE"])
def logout():
    session.pop("username")
    return jsonify(msg="退出登录成功")

