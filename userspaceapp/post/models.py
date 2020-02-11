from userspaceapp import db
from flask_login import UserMixin


class Post(db.Model):

    __tablename__='posts'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    content=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))