# **************************************** /users/forms.py ****************************************

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from userspaceapp.users.models import User

class LoginForm(FlaskForm):

    username=StringField('enter username',validators=[DataRequired(),Email()])
    password=PasswordField('enter password',validators=[DataRequired()])
    login=SubmitField('login')

class RegisterForm(FlaskForm):

    username=StringField('enter username',validators=[DataRequired()])
    email=StringField('enter email',validators=[DataRequired(),Email()])
    password=PasswordField('enter password',validators=[DataRequired()])
    confirm_password=PasswordField('enter confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('register')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username is already taken')
    
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is already taken')


class UpdateInfoForm(FlaskForm):

    username=StringField('username',validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired(),Email()])
    submit=SubmitField('update')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if not user:
            flash('username updated')
    
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if not user:
            flash('email updated')
