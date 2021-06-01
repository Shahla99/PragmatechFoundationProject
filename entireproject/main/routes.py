from app import app
from app.models import About, Beginner, Camps, Comment, Contact, Gallery, Language, Lesson, Pro, Slider, User, column_control, galleryimage, generic_block, social_media
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,request,redirect,url_for,make_response
from app import bc

@app.route('/')
def main_index():
    lessons=Lesson.query.all()
    languages=Language.query.all()
    columns=column_control.query.all()
    generic=generic_block.query.all()
    social=social_media.query.all()
    aboutt=about.query.all()
    gallerys=Gallery.query.all()
    galleryimages=galleryimage.query.all()
    contacts = Contact.query.all()
    comments = Comment.query.all()
    return render_template('main/index.html', lessons=lessons, languages=languages,columns=columns, generic=generic, social=social,aboutt=aboutt,gallerys=gallerys,galleryimages=galleryimages,contacts=contacts,comments=comments)
    
@app.route('/slider/')
def main_slider():
    slides=Slider.query.all()
    social=social_media.query.all()
    return render_template('main/beginners.html',beginners=beginners,social=social,slides=slides)


@app.route('/beginners/')
def main_beginners():
    beginners=Beginner.query.all()
    social=social_media.query.all()
    return render_template('main/beginners.html',beginners=beginners,social=social)

@app.route('/pro/')
def main_pro():
    pro=Pro.query.all()
    social=social_media.query.all()
    return render_template('main/pro.html',pro=pro,social=social)

@app.route('/camps/')
def main_camps():
    camps=Camps.query.all()
    social=social_media.query.all()
    return render_template('main/camps.html',camps=camps,social=social)

@app.route('/about/')
def main_about():
    aboutt=About.query.all()
    social=social_media.query.all()
    return render_template('main/about.html',aboutt=aboutt,social=social)

@app.route('/contact/')
def main_contact():
    return render_template('main/contact.html')

@app.route('/gallery/')
def main_gallery():
    gallerys=gallery.query.all()
    galleryimages=galleryimage.query.all()
    social=social_media.query.all()
    return render_template('main/gallery.html',gallerys=gallerys,social=social,galleryimages=galleryimages)


@app.route('/login/',methods=['GET','POST']) 
def main_login():
    users=User.query.all()
    social=social_media.query.all()
    loginStat = request.cookies.get('loginStatus')
    loginId = 'Hello'
    for user in users:
        if str(user.id) == loginStat:
            loginId=str(user.id)
    if request.method == 'POST':
        for user in users:
            if user.email == request.form['email']:
                if bc.check_password_hash(user.password,request.form['password']):
                    loginId = str(user.id)
                    loginStat=loginId
                    resp=make_response(render_template('main/profile.html',user=user,social=social,loginStat=loginStat,loginId=loginId))
                    resp.set_cookie('loginStatus',str(user.id))
                    return resp 
                else:
                    return redirect('/main/login')

    return render_template('main/login.html',user=user,social=social,loginStat=loginStat,loginId=loginId)
       

@app.route('/register/',methods=['GET','POST']) 
def main_register():
    users=User.query.all()
    social=social_media.query.all()
    loginStat = request.cookies.get('loginStatus')
    if request.method == 'POST':
        users=User(
            fullname=request.form['fullname'],
            email=request.form['email'],
            password=bc.generate_password_hash(request.form['password'])
        )
        db.session.add(User)
        db.session.commit()
        return redirect (url_for('main_login'))
    return render_template('main/register.html',users=users,social=social,loginStat=loginStat)

@app.route('/logout/',methods=['GET','POST']) 
def logout():
    lessons=Lesson.query.all()
    languages=Language.query.all()
    columns=column_control.query.all()
    generic=generic_block.query.all()
    social=social_media.query.all()
    aboutt=about.query.all()
    gallerys=Gallery.query.all()
    galleryimages=galleryimage.query.all()
    contacts = Contact.query.all()
    comments = Comment.query.all()
    loginStat = request.cookies.get('loginStatus')
    users=User.query.all()
    loginId=''
    for user in users:
         if user.id==loginStat:
             loginId=str(loginStat)
    resp=make_response(render_template('main/index.html',user=user,social=social,loginStat=loginStat,loginId=loginId,lessons=lessons,aboutt=aboutt, languages=languages,columns=columns, generic=generic,gallerys=gallerys,galleryimages=galleryimages,contacts=contacts,comments=comments))
    resp.set_cookie('loginStatus','logout')
    return resp 

@app.route('main/contact/', methods=['GET','POST'])
def main_contact(id):
    contacts = Contact.query.all()
    comments = Comment.query.all()
    if request.method=='POST':
      comments = Comment(
        c_name=request.form['c_name'],
        c_surname=request.form['c_surname'],
        c_email=request.form['c_email'],
        c_message=request.form['c_message'],
        contact_id=id
      )
      db.session.add(Comment)
      db.session.commit()
      return redirect(url_for('main_contact', id=id))
    return render_template('main/contact.html', contacts=contacts,comments=comments)