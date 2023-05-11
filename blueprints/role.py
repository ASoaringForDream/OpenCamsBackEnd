from flask import Blueprint, request, jsonify
from models.role import Role
from models.manager import Manager
from exts import db as datebase



db = Blueprint("character", __name__, url_prefix='/manager')

@db.route('/characters', methods=['GET'])
def queryCharacters():
    data = request.args
    current = int(data.get('current'))
    pageSize = int(data.get('pageSize'))
    allRoles = Role.query.all()
    roles = Role.query.offset((current - 1) * pageSize).limit(pageSize).all()
    res = []
    for item in roles:
        res.append(item.to_json())
    return {
        "errno": 0,
        "errmsg": '',
        "data":{
            "total": len(allRoles),
            "data": res
        }
    }

@db.route('/addcharacter', methods=['POST'])
def addCharacters():
    data = request.get_json(silent=True)
    name = data.get('name')
    role_ids = data.get('role_ids')
    role_desc = data.get('role_desc')

    role = Role(name=name, role_ids=role_ids, role_desc=role_desc)
    datebase.session.add(role)
    datebase.session.commit()

    return {
        "errno": 0,
        "errmsg":''
    }

@db.route('/deletecharacter', methods=['DELETE'])
def deleteCharacter():
    data = request.get_json(silent=True)
    id = data.get('id')
    manager = Manager.query.filter(Manager.role == id).first()
    if manager != None:
        return jsonify({
            "errno": 1,
            "errmsg": '当前存在管理员属于该角色'
        })
    Role.query.filter(Role.id == id).delete()
    # datebase.session.delete(manager)
    datebase.session.commit()
    return jsonify({
        "errno": 0,
        "errmsg": ''
    })

@db.route('/editcharacter', methods=['POST'])
def editCharacter():
    data = request.get_json(silent=True)
    id = data.get('id')
    name = data.get('name')
    role_ids = data.get('role_ids')
    role_desc = data.get('role_desc')
    role = Role.query.filter(Role.id == id).first()
    role.name = name
    role.role_ids = role_ids
    role.role_desc = role_desc
    datebase.session.commit()

    return {
        "errno": 0,
        "errmsg":''
    }
