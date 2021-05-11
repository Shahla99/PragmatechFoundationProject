from app import app 
from app.models import Slider
from flask import render_template,request,redirect

@app.route('/')
def main_index():
    slides=Slider.query.all()
    return render_template('main/index.html',slides=slides)