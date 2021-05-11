from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SECRET_KEY']='567bb980bas'
UPLOAD_FOLDER='app/static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
db=SQLAlchemy(app)



from app.models import *


from admin.routes import *



from main.routes import *