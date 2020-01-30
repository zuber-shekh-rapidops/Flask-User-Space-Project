from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo


class LoginForm(FlaskForm):

    username=StringField('enter username',validators=[DataRequired(),Email()])
    password=PasswordField('enter password',validators=[DataRequired()])
    login=SubmitField('login')

class RegisterForm(FlaskForm):

    username=StringField('enter username',validators=[DataRequired()])
    email=StringField('enter email',validators=[DataRequired(),Email()])
    password=PasswordField('enter password',validators=[DataRequired()])
    confirm_password=PasswordField('enter confirm password',validators=[DataRequired(),EqualTo('password')])
    register=SubmitField('register')

