from flask import Flask
from config import DevelopmentConfig
from exts import config_extensions
from blueprints import config_blueprint
from flask_cors import CORS
from exts import db as datebase
from models.cam import Cam
import requests
import json

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='http://localhost:7000')

app.config.from_object(DevelopmentConfig)
config_extensions(app)
config_blueprint(app)

@app.route('/')
def print_hi():
    with open('C:\\Users\\86176\\Desktop\\pythonProject\\flv.json', mode='r+') as f:
        list = json.loads(f.read())
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        }
        for idx in range(len(list)):
            print(idx)
            curr = list[idx]
            posterImg = requests.get(curr['thumbnail_large'], headers=headers)
            with open(f'C:\DUT\openCamsPosterImg\{curr["id"]}.jpg', mode='wb') as f:
                f.write(posterImg.content)
            cam = Cam(tit=curr['title'], source=curr['sUrl'], desc=curr['description'], origin=curr['url'], postImg=[f'C:\DUT\openCamsPosterImg\{curr["id"]}.jpg'],
                      country=curr['country'], state=curr['state_full'], city=curr['city'], type='iframe')
            datebase.session.add(cam)
            datebase.session.commit()

if __name__ == '__main__':
    app.run(debug=True, port=3389)
