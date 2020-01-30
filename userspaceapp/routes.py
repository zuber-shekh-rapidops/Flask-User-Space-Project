from userspaceapp import app
from userspaceapp.forms import LoginForm,RegisterForm
from flask import render_template,redirect,url_for

#  ******************************** ROUTES ******************************** 
#  ******************************** / ******************************** 

@app.route('/')
def index():
    return render_template('index.html')
#  ******************************** /LOGIN ******************************** 
@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',form=form)
#  ******************************** /REGISTER ******************************** 
@app.route('/register')
def register():
    form=RegisterForm()
    return render_template('register.html',form=form)
#  ******************************** /USER/HOME ******************************** 
