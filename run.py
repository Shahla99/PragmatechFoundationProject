from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


#admin routes

from controllers.admin.routes import *

from controllers.main.routes import * 

if __name__=='__main__':
    app.run(debug=True)