# **************************************** /users/models.py ****************************************

from userspaceapp import db,login_manager,bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def login_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=False)
    password=db.Column(db.String(30),nullable=False)
    posts=db.relationship('Post',backref='user')

    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)

    def __repr__(self):
        return f"Hello I am {self.username}"



    


