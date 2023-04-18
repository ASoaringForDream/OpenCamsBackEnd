from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from models.user import User
from exts import db as datebase



db = Blueprint("user", __name__, url_prefix='/manager')

@db.route('/users', methods=['GET'])
def queryUsers():
    data = request.args
    username = data.get('username')
    id = data.get('id')
    state = data.get('state')
    current = int(data.get('current'))
    pageSize = int(data.get('pageSize'))
    allUsers = User.query.filter(
        or_(User.id == id, id == None, id == ''),
        or_(username == None, User.username.like('%' + str(username) + '%'), username == ''),
        or_(User.state == state, state == None, state == '')).all()
    users = User.query.filter(
        or_(User.id == id, id == None, id == ''),
        or_(username == None, User.username.like('%' + str(username) + '%'), username == ''),
        or_(User.state == state, state == None, state == '')).offset((current - 1) * pageSize).limit(pageSize).all()
    res = []
    for item in users:
        res.append(item.to_json())
    return {
        "errno": 0,
        "errmsg": '',
        "data":{
            "total": len(allUsers),
            "data": res
        }
    }

@db.route('/adduser', methods=['POST'])
def addUser():
    data = request.get_json(silent=True)
    username = data.get('username')
    password = data.get('password')
    state = data.get('state')
    name = data.get('name')
    sex = data.get('sex')
    birth = data.get('birth')
    telephone = data.get('telephone')
    mailbox = data.get('mailbox')
    userpic = data.get('userpic')

    curr = User.query.filter(User.username == username).first()
    if curr != None:
        return {
            "errno": 1,
            "errmsg": '用户名已存在!'
        }
    else:
        curr = User.query.filter(User.mailbox == mailbox).first()
        if curr !=None:
            return {
                "errno": 1,
                "errmsg": '邮箱已存在!'
            }
    user = User(username=username, password=password, state=state, name=name, sex=sex, telephone=telephone, mailbox=mailbox, userpic=userpic, birth=birth)
    datebase.session.add(user)
    datebase.session.commit()

    return {
        "errno": 0,
        "errmsg":''
    }

@db.route('/deleteuser', methods=['DELETE'])
def delUser():
    data = request.get_json(silent=True)
    id = data.get('id')
    User.query.filter(User.id == id).delete()
    # datebase.session.delete(manager)
    datebase.session.commit()
    return jsonify({
        "errno": 0,
        "errmsg": ''
    })

@db.route('/edituser', methods=['POST'])
def editUser():
    data = request.get_json(silent=True)
    id = data.get('id')
    password = data.get('password')
    state = data.get('state')
    name = data.get('name')
    sex = data.get('sex')
    birth = data.get('birth')
    telephone = data.get('telephone')
    mailbox = data.get('mailbox')
    userpic = data.get('userpic')

    user = User.query.filter(User.id == id).first()
    if password != None:
        user.password = password
    if state != None:
        user.state = state
    if name != None:
        user.name = name
    if sex != None:
        user.sex = sex
    if birth != None:
        user.birth = birth
    if telephone != None:
        user.telephone = telephone
    if mailbox != None:
        curr = User.query.filter(User.mailbox == mailbox).first()
        if curr != None and curr.id != id:
            return {
                "errno": 1,
                "errmsg": '邮箱已存在!'
            }
        user.mailbox = mailbox
    if userpic != None:
        user.userpic = userpic
    datebase.session.commit()

    return {
        "errno": 0,
        "errmsg":''
    }

@db.route('/banuser', methods=['POST'])
def banUser():
    data = request.get_json(silent=True)
    id = data.get('id')
    state = data.get('state')

    user = User.query.filter(User.id == id).first()
    if state != None:
        user.state = state
    datebase.session.commit()

    return {
        "errno": 0,
        "errmsg":''
    }