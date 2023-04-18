from flask import Blueprint, request, jsonify, session, make_response
import time
from sqlalchemy import or_
from models.manager import Manager
from models.user import User
from models.role import Role, Roleitem
from exts import db as datebase



db = Blueprint("manager", __name__, url_prefix='/manager')

@db.route('/managers', methods=['GET'])
def queryManagers():
    data = request.args
    username = data.get('username')
    id = data.get('id')
    role = data.get('role')
    current = int(data.get('current'))
    pageSize = int(data.get('pageSize'))
    allManagers = Manager.query.filter(
        or_(Manager.id == id, id == None, id == ''),
        or_(username == None, Manager.username.like('%' + str(username) + '%'), username == ''),
        or_(Manager.role == role, role == None, role == '')).all()
    managers = Manager.query.filter(
        or_(Manager.id == id, id == None, id == ''),
        or_(username == None, Manager.username.like('%' + str(username) + '%'), username == ''),
        or_(Manager.role == role, role == None, role == '')).offset((current - 1) * pageSize).limit(pageSize).all()
    res = []
    for item in managers:
        res.append(item.to_json())
    return {
        "errno": 0,
        "errmsg": '',
        "data":{
            "total": len(allManagers),
            "data": res
        }
    }

@db.route('/roles', methods=['GET'])
def queryRoles():
    roles = Role.query.all()
    res = []
    for item in roles:
        res.append(item.to_json())
    return {
        "errno": 0,
        "errmsg": '',
        "data": res
    }

@db.route('/addmanager', methods=['POST'])
def addManager():
    data = request.get_json(silent=True)
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    name = data.get('name')
    sex = data.get('sex')
    birth = data.get('birth')
    telephone = data.get('telephone')
    mailbox = data.get('mailbox')
    userpic = data.get('userpic')
    # birth = time.strftime("%Y-%m-%d", birth)
    print(birth)

    curr = Manager.query.filter(Manager.username == username).first()
    if curr != None:
        return {
            "errno": 1,
            "errmsg": '用户名已存在!'
        }
    else:
        curr = Manager.query.filter(Manager.mailbox == mailbox).first()
        if curr !=None:
            return {
                "errno": 1,
                "errmsg": '邮箱已存在!'
            }
    manager = Manager(username=username, password=password, role=role, name=name, sex=sex, telephone=telephone, mailbox=mailbox, userpic=userpic, birth=birth)
    datebase.session.add(manager)
    datebase.session.commit()


    return {
        "errno": 0,
        "errmsg":''
    }

@db.route('/deletemanager', methods=['DELETE'])
def delManager():
    data = request.get_json(silent=True)
    id = data.get('id')
    manager = Manager.query.filter(Manager.id == id).delete()
    # datebase.session.delete(manager)
    datebase.session.commit()
    return jsonify({
        "errno": 0,
        "errmsg": ''
    })

@db.route('/editmanager', methods=['POST'])
def editManager():
    data = request.get_json(silent=True)
    id = data.get('id')
    password = data.get('password')
    role = data.get('role')
    name = data.get('name')
    sex = data.get('sex')
    birth = data.get('birth')
    telephone = data.get('telephone')
    mailbox = data.get('mailbox')
    userpic = data.get('userpic')

    manager = Manager.query.filter(Manager.id == id).first()
    if password != None:
        manager.password = password
    if role != None:
        manager.role = role
    if name != None:
        manager.name = name
    if sex != None:
        manager.sex = sex
    if birth != None:
        manager.birth = birth
    if telephone != None:
        manager.telephone = telephone
    if mailbox != None:
        manager.mailbox = mailbox
    if userpic != None:
        manager.userpic = userpic
    datebase.session.commit()

    return {
        "errno": 0,
        "errmsg":''
    }