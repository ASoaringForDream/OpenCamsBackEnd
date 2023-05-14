from flask import Flask, send_file
from config import DevelopmentConfig
from exts import config_extensions
from blueprints import config_blueprint
from flask_cors import CORS
from exts import db as datebase
from models.cam import Cam
import requests
import json
from pygtrans import Translate

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='http://localhost:7000')

app.config.from_object(DevelopmentConfig)
config_extensions(app)
config_blueprint(app)

@app.route('/manage/img/<name>')
def getImg(name):
    return send_file(f'C:\\DUT\\openCamsPosterImg\\{name}', mimetype="image/jpeg")
    # with open('C:\\Users\\86176\\Desktop\\pythonProject\\y.json', mode='r+') as f:
    #     list = json.loads(f.read())
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
    #     }
    #     client = Translate()
    #     for idx in range(len(list)):
    #         print(idx)
    #         curr = list[idx]
    #         if '?' in curr["id"]:
    #             curr["id"] = curr["id"].split('?')[0]
    #         posterImg = requests.get(curr['thumbnail_large'], headers=headers)
    #         with open(f'C:\DUT\openCamsPosterImg\{curr["id"]}.jpg', mode='wb') as f:
    #             f.write(posterImg.content)
    #         # print(curr)
    #         if 'state_full' not in curr or curr['state_full'] == None:
    #             state = None
    #         else:
    #             state = client.translate(curr['state_full']).translatedText
    #         cam = Cam(tit=client.translate(curr['title'] + 'era').translatedText, source=curr['sUrl'], desc=client.translate(curr['description']).translatedText, origin=curr['url'], originId=curr['id'],
    #                   posterImg=f'{curr["id"]}.jpg', posterImgPath=f'C:\DUT\openCamsPosterImg\{curr["id"]}.jpg', score = 10, clickcount = 10,
    #                   country=client.translate(curr['country']).translatedText, state=state, city=client.translate(curr['city']).translatedText, type='iframe')
    #         datebase.session.add(cam)
    #         datebase.session.commit()

if __name__ == '__main__':
    app.run(debug=True, port=3389)
