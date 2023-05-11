from exts import db

class Cam(db.Model):
    __tablename__ = "cam"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tit = db.Column(db.Text, nullable=False)
    source = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    origin = db.Column(db.Text, nullable=False)
    like = db.Column(db.Integer, default=0, nullable=False)
    dislike = db.Column(db.Integer, default=0, nullable=False)
    clickcount = db.Column(db.Integer, default=0, nullable=False)
    type = db.Column(db.Enum("iframe", "HLS"), nullable=False)
    tag = db.Column(db.Text)
    mainTag = db.Column(db.Integer)
    postImg = db.Column(db.String(512))
    country = db.Column(db.String(256))
    state = db.Column(db.String(256))
    city = db.Column(db.String(256))

    def to_json(self):
        return {
            "id": self.id,
            "tit": self.tit,
            "source": self.source,
            "desc": self.desc,
            "origin": self.origin,
            "like": self.like,
            "clickcount": self.clickcount,
            "tag": self.tag,
            "mainTag": self.mainTag,
            "country": self.country,
            "city": self.city
        }