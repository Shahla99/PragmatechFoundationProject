from app import db

class Slider(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    s_title=db.Column(db.String(50))
    s_text=db.Column(db.String(50))
    s_url=db.Column(db.String(50))
    s_image=db.Column(db.String(50))

