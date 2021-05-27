from app import app
from app import db
from app.models import Beginners, Camps, Language, Lesson, Pro, Slider, Sliderimage, User, about, column_control, gallery, galleryimage, generic_block, social_media
import os 
from flask import render_template,redirect,request

@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')


@app.route('/admin/slider',methods=['GET','POST'])
def admin_slider():
    slides=Slider.query.all()
    if request.method=='POST':
        file=request.files['slider_photo']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        slide=Slider(
            slider_title=request.form['slider_title'],
            slider_text=request.form['slider_text'],
            slider_url=request.form['slider_url'],
            slider_photo=filename
        )
        db.session.add(Slider)
        db.session.commit()
        return redirect('/admin/slider')
    return render_template('admin/slider.html',slides=slides) 

@app.route('/admin/lesson',methods=['GET','POST'])
def admin_lesson():
    lessons=Lesson.query.all()
    if request.method=='POST':
        file=request.files['lesson_logo']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        lessons=Lesson(
            lesson_name=request.form['lesson_name'],
            lesson_text=request.form['lesson_text'],
            lesson_url=request.form['lesson_url'],
            lesson_content=request.form['lesson_content'],
            lesson_details=request.form['lesson_details'],
            lesson_logo=filename
        )
        db.session.add(Lesson)
        db.session.commit()
        return redirect('/admin/lesson')
    return render_template('admin/lesson.html',lessons=lessons)
