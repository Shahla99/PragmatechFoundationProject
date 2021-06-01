from app import app
from app import db
from app.models import About, Beginner, Camps, Comment, Contact, Gallery, Lesson, Pro, Slider, column_control, generic_block, social_media
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


        slides=Slider(
            slider_title=request.form['slider_title'],
            slider_text=request.form['slider_text'],
            slider_url=request.form['slider_url'],
            slider_photo=filename
        )
        db.session.add(Slider)
        db.session.commit()
        return redirect('/admin/slider/')
    return render_template('admin/slider.html/',slides=slides) 



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

@app.route('/admin/column_control',methods=['GET','POST'])
def admin_column_control():
    columns=column_control.query.all()
    if request.method=='POST':
        file=request.files['column_control_logo']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        columns=column_control(
            column_control_header=request.form['column_control_header'],
            column_control_text=request.form['column_control_text']
        )
        db.session.add(column_control)
        db.session.commit()
        return redirect('/admin/column_control')
    return render_template('admin/column_control.html',columns=columns)

@app.route('/admin/generic_block',methods=['GET','POST'])
def admin_generic_block():
    generic_blocks=generic_block.query.all()
    if request.method=='POST':
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        generic_blocks=generic_block(
            generic_block_title=request.form['generic_block_title'],
            generic_block_text=request.form['generic_block_text']
        )
        db.session.add(generic_block)
        db.session.commit()
        return redirect('/admin/generic_block')
    return render_template('/admin/generic_block.html',generic_blocks=generic_blocks)


@app.route('/admin/beginner',methods=['GET','POST'])
def admin_beginner():
    beginners=Beginner.query.all()
    if request.method=='POST':
        file=request.files['beginner_image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        beginners=Beginner(
            beginner_title=request.form['beginner_title'],
            beginner_info=request.form['beginner_info'],
            beginner_details=request.form['beginner_details'],
            beginner_link=request.form['beginner_link'],
            beginner_image=filename
        )
        db.session.add(Beginner)
        db.session.commit()
        return redirect('/admin/beginners')
    return render_template('admin/beginners.html',beginners=beginners)


@app.route('/admin/pro',methods=['GET','POST'])
def admin_pro():
    pro=Pro.query.all()
    if request.method=='POST':
        file=request.files['pro_image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        pro=Pro(
            pro_title=request.form['pro_title'],
            pro_info=request.form['pro_info'],
            pro_details=request.form['pro_details'],
            pro_link=request.form['pro_link'],
            pro_image=filename
        )
        db.session.add(Pro)
        db.session.commit()
        return redirect('/admin/pros')
    return render_template('admin/pro.html',pro=pro)


@app.route('/admin/camps',methods=['GET','POST'])
def admin_camps():
    camps=Camps.query.all()
    if request.method=='POST':
        file=request.files['camps_image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        camps=Camps(
            camps_title=request.form['camps_title'],
            camps_info=request.form['camps_info'],
            camps_details=request.form['camps_details'],
            camps_link=request.form['camps_link'],
            camps_image=filename
        )
        db.session.add(Camps)
        db.session.commit()
        return redirect('/admin/campss')
    return render_template('admin/camps.html',camps=camps)


@app.route('/admin/contact',methods=['GET','POST'])
def admin_contact():
    contacts=Contact.query.all()
    if request.method=='POST':
        contacts=Contact(
            contact_icon=request.form['contact_icon'],
            contact_phone=request.form['contact_phone'],
            contact_email=request.form['contact_email'],
            contact_title=request.form['contact_title']
        )
        db.session.add(Contact)
        db.session.commit()
        return redirect('/admin/contact')
    return render_template('admin/contact.html',contacts=contacts)

@app.route('/admin/social_media',methods=['GET','POST'])
def admin_social_media():
    social=social_media.query.all()
    if request.method=='POST':
        social=social_media(
            social_icon=request.form['social_icon'],
            social_url=request.form['social_url']
        )
        db.session.add(social_media)
        db.session.commit()
        return redirect('/admin/social_media')
    return render_template('admin/socialmedia.html',social=social)

@app.route('/admin/contact/comment')
def admin_contact_comment():
    comments=Comment.query.all()
    return render_template('/admin/contact_comment.html',comments=comments)


@app.route('/admin/about',methods=['GET','POST'])
def admin_about():
    aboutt=About.query.all()
    if request.method=='POST':
        file=request.files['about_image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        aboutt=About(
            about_header=request.form['about_header'],
            about_text=request.form['about_text'],
            about_image=filename
        )
        db.session.add(About)
        db.session.commit()
        return redirect('/admin/aboutt')
    return render_template('admin/about.html',aboutt=aboutt)

@app.route('/admin/gallery',methods=['GET','POST'])
def admin_gallery():
    gallerys=Gallery.query.all()
    if request.method=='POST':
        file=request.files['gallery_photo']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))


        gallerys=Gallery(
            gallery_photo=filename
        )
        db.session.add(Gallery)
        db.session.commit()
        return redirect('/admin/gallery')
    return render_template('admin/gallery.html',gallerys=gallerys)

