from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from models.cam import Cam, CamMainTag, CamTag
from exts import db as datebase



db = Blueprint("cam", __name__, url_prefix='/manager')

@db.route('/cams', methods=['GET'])
def queryCams():
    data = request.args
    tit = data.get('tit')
    id = data.get('id')
    mainTag = data.get('mainTag')
    current = int(data.get('current'))
    pageSize = int(data.get('pageSize'))
    allCams = Cam.query.filter(
        or_(Cam.id == id, id == None, id == ''),
        or_(tit == None, Cam.tit.like('%' + str(tit) + '%'), tit == ''),
        or_(Cam.mainTag == mainTag, mainTag == None, mainTag == '')).all()
    cams = Cam.query.filter(
        or_(Cam.id == id, id == None, id == ''),
        or_(tit == None, Cam.tit.like('%' + str(tit) + '%'), tit == ''),
        or_(Cam.mainTag == mainTag, mainTag == None, mainTag == '')).offset((current - 1) * pageSize).limit(pageSize).all()
    res = []
    for item in cams:
        res.append(item.to_json())
    return {
        "errno": 0,
        "errmsg": '',
        "data":{
            "total": len(allCams),
            "data": res
        }
    }
@db.route('/deletecam', methods=['DELETE'])
def delCam():
    data = request.get_json(silent=True)
    id = data.get('id')
    cam = Cam.query.filter(Cam.id == id).delete()
    # datebase.session.delete(manager)
    datebase.session.commit()
    return jsonify({
        "errno": 0,
        "errmsg": ''
    })

@db.route('/editcam', methods=['POST'])
def editManager():
    data = request.get_json(silent=True)
    id = data.get('id')
    tit = data.get('tit')
    desc = data.get('desc')
    tag = data.get('tag')
    mainTag = data.get('mainTag')

    cam = Cam.query.filter(Cam.id == id).first()
    if tit != None:
        cam.tit = tit
    if desc != None:
        cam.role = desc
    if mainTag != None:
        cam.mainTag = mainTag
    if tag != None:
        cam.tag = tag
    datebase.session.commit()

    return {
        "errno": 0,
        "errmsg":''
    }

@db.route('/camtags', methods=['GET'])
def querycamtags():
    camMainTags = CamMainTag.query.all()
    camTags = CamTag.query.all()
    main = []
    for item in camMainTags:
        main.append(item.to_json())
    tag = []
    for item in camTags:
        tag.append(item.to_json())
    return {
        "errno": 0,
        "errmsg": '',
        "data": {
            "data": main,
            "tags": tag
        }
    }