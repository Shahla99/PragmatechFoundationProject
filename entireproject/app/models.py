from app import db

class Slider(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    slider_title=db.Column(db.String(50))
    slider_text=db.Column(db.String(50))
    slider_url=db.Column(db.String(50))
    slider_photo=db.Column(db.String(50))
    images=db.relationship('sliderimage',backref='slider')
    

class Sliderimage(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    img_src=db.Column(db.String(50))
    slider_id=db.Column(db.Integer, db.ForeignKey('slider_id'),nullable=False)


class Lesson(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    lesson_name=db.Column(db.String(50))
    lesson_text=db.Column(db.String(50))
    lesson_url=db.Column(db.String(50))
    lesson_content=db.Column(db.String(50))
    lesson_logo=db.Column(db.String(50)) 
    lesson_details=db.Column(db.String(100))
    languages=db.relationship('Language',backref='lesson') 
    

class Language(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    language_name=db.Column(db.String(50))
    language_text=db.Column(db.String(50))
    language_image=db.Column(db.String(100))
    language_content=db.Column(db.String(50))
    lesson_id=db.Column(db.Integer, db.ForeignKey('lesson_id'),nullable=False)

  
class column_control(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    column_header=db.Column(db.String(50))
    column_title=db.Column(db.String(50))
    column_text=db.Column(db.String(50)) 
    column_logo=db.Column(db.String(100)) 
    

class generic_block(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    generic_title=db.Column(db.String(50))
    generic_text=db.Column(db.String(100))
    generic_image=db.Column(db.String(50)) 

class social_media(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    social_icon=db.Column(db.String(50))
    social_url=db.Column(db.String(100))

class Beginners(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    beginners_title=db.Column(db.String(50))
    beginners_info=db.Column(db.String(100))
    beginners_image=db.Column(db.String(50)) 
    beginners_details=db.Column(db.String(50)) 
    beginners_link=db.Column(db.String(50)) 

class Pro(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    pro_title=db.Column(db.String(50))
    pro_info=db.Column(db.String(100))
    pro_image=db.Column(db.String(50)) 
    pro_details=db.Column(db.String(50)) 
    pro_link=db.Column(db.String(50)) 

class Camps(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    camps_title=db.Column(db.String(50))
    camps_info=db.Column(db.String(100))
    camps_image=db.Column(db.String(50)) 
    camps_details=db.Column(db.String(50)) 
    camps_link=db.Column(db.String(50)) 

class about(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_image=db.Column(db.String(50))
    about_header=db.Column(db.String(50))
    about_text=db.Column(db.String(50))

class gallery(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    gallery_photo=db.Column(db.String(50))
    gallerys=db.relationship('galleryimage',backref='gallery')

class galleryimage(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    img_src=db.Column(db.String(50))
    gallery_id=db.Column(db.Integer, db.ForeignKey('gallery_id'),nullable=False)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    password=db.Column(db.String(50))
    email=db.Column(db.String(50))
    fullname=db.Column(db.String(100))

