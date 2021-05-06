from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
UPLOAD_FOLDER='/static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
db=SQLAlchemy(app)

from models import *

from admin.routes import *

from main.routes import *

db.create_all()

