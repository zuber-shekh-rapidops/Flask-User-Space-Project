from userspaceapp import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def login_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=False)
    password=db.Column(db.String(30),nullable=False)


    def __repr__(self):
        return f"Hello I am {self.username}"
