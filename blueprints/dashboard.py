import datetime

from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from models.cam import Cam, CamMainTag, CamTag
from models.user import User
from models.operation import Visit, Collect, Like, DisLike

db = Blueprint("dashboard", __name__, url_prefix='/manager')

@db.route('/dashboard', methods=['GET'])
def dashBoard():
    userCount = User.query.count()
    camCount = Cam.query.count()
    userAddToday = User.query.filter(User.creattime > datetime.date.today()).count()
    allVisitCount = Visit.query.count()
    visitCount1 = Visit.query.filter(Visit.visittime > datetime.date.today()).count()
    time = datetime.timedelta(days=1)
    visitCount2 = Visit.query.filter(Visit.visittime > datetime.date.today() - time, Visit.visittime <= datetime.date.today() ).count()
    time1 = datetime.timedelta(days=1)
    time = datetime.timedelta(days=2)
    visitCount3 = Visit.query.filter(Visit.visittime > datetime.date.today() - time, Visit.visittime <= datetime.date.today() - time1).count()
    ime1 = datetime.timedelta(days=2)
    time = datetime.timedelta(days=3)
    visitCount4 = Visit.query.filter(Visit.visittime > datetime.date.today() - time, Visit.visittime <= datetime.date.today() - time1).count()
    ime1 = datetime.timedelta(days=3)
    time = datetime.timedelta(days=4)
    visitCount5 = Visit.query.filter(Visit.visittime > datetime.date.today() - time, Visit.visittime <= datetime.date.today() - time1).count()
    mainTags = CamMainTag.query.all()
    res = []
    print(userCount)
    print(camCount)
    print(userAddToday)
    print(allVisitCount)
    print([visitCount5, visitCount4, visitCount3, visitCount2, visitCount1])
    for item in mainTags:
        cams = Cam.query.filter(Cam.mainTag == item.id).count()
        res.append(item.to_json1(cams))
    return {
        "errno": 0,
        "errmsg": '',
        "data": {
            "userCount": userCount,
            "camCount": camCount,
            "userAddToday": userAddToday,
            "allVisitCount": allVisitCount,
            "visitAdd": [visitCount5, visitCount4, visitCount3, visitCount2, visitCount1],
            "tagCount":res
        }
    }