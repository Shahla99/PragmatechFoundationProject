from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']='567bb980ghas'
UPLOAD_FOLDER='app/static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
db=SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)



from app.models import *


from admin.routes import *


from main.routes import *


from auth.routes import *


