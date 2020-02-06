import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
#  ******************************** CONFIGURATIONS ******************************** 
BASEDIR=os.path.abspath(os.path.dirname(__name__))
app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASEDIR,'userspaceapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

login_manager=LoginManager(app)
Migrate(app,db)
bcrypt=Bcrypt(app)
#  ********************************  ******************************** 

from userspaceapp.main.routes import main
from userspaceapp.users.routes import users


app.register_blueprint(main)
app.register_blueprint(users)

from userspaceapp.main import routes
from userspaceapp.users import routes