from app import app
from app.models import Beginners, Camps, Language, Lesson, Pro, Slider, Sliderimage, User, about, column_control, gallery, galleryimage, generic_block, social_media
from flask_sqlalchemy import sqlalchemy
from flask import render_template,request,redirect

@app.route('/')
def main_index():
    slides=Slider.query.all()
    images=Sliderimage.query.all()
    lessons=Lesson.query.all()
    languages=Language.query.all()
    columns=column_control.query.all()
    generic=generic_block.query.all()
    social=social_media.query.all()
    aboutt=about.query.all()
    gallerys=gallery.query.all()
    galleryimages=galleryimage.query.all()
    return render_template('main/index.html', slides=slides, lessons=lessons, languages=languages,columns=columns, generic=generic, social=social,images=images,aboutt=aboutt,gallerys=gallerys,galleryimages=galleryimages)
    
@app.route('/beginners')
def main_beginners():
    beginner=Beginners.query.all()
    social=social_media.query.all()
    return render_template('main/beginners.html',beginner=beginner,social=social)

@app.route('/pro')
def main_pro():
    pro=Pro.query.all()
    social=social_media.query.all()
    return render_template('main/pro.html',pro=pro,social=social)

@app.route('/camps')
def main_camps():
    camps=Camps.query.all()
    social=social_media.query.all()
    return render_template('main/camps.html',camps=camps,social=social)

@app.route('/about')
def main_about():
    aboutt=about.query.all()
    social=social_media.query.all()
    return render_template('main/about.html',aboutt=aboutt,social=social)

@app.route('/contact')
def main_contact():
    return render_template('main/contact.html')

@app.route('/gallery')
def main_gallery():
    gallerys=gallery.query.all()
    galleryimages=galleryimage.query.all()
    social=social_media.query.all()
    return render_template('main/gallery.html',gallerys=gallerys,social=social,galleryimages=galleryimages)

@app.route('/js')
def main_js():
    return render_template('main/languages.html')

@app.route('/login',methods=['GET','POST']) 
def main_login():
    users=User.query.all(
        username = request.form['username'],
        password = request.form['password'] 
        
)
    return render_template('main/login.html',users=users)
