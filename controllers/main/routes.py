from run import app
from flask import render_template,request,redirect

@app.route('/')
def main_index():
    return render_template('main/index.html')
