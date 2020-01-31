from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#  ******************************** CONFIGURATIONS ******************************** 
app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///userspace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
login_manager=LoginManager(app)
#  ********************************  ******************************** 
from userspaceapp import routes