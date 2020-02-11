#  ******************************** /users/routes.py ******************************** 
from userspaceapp import db
from userspaceapp.users.forms import LoginForm,RegisterForm,UpdateInfoForm
from userspaceapp.users.models import User
from flask import render_template,redirect,url_for,flash,request,Blueprint
from flask_login import login_user,logout_user,login_required,current_user

users=Blueprint('users',__name__)
#  ******************************** ROUTES ******************************** 
#  ******************************** /LOGIN ******************************** 
@users.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    form=LoginForm()

    if form.validate_on_submit():
        user=User.query.filter_by(email=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash('login successfull')
            login_user(user)
            return redirect(url_for('users.home'))
        else:
            flash('incorrect username or password')
            return redirect(url_for('users.login'))

    return render_template('login.html',form=form)
#  ******************************** /REGISTER ******************************** 
@users.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account created successfully')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)
#  ******************************** /HOME ******************************** 
@users.route('/home')
@login_required
def home():
    users=User.query.all()
    return render_template('home.html',users=users)
#  ******************************** /ACCOUNT ******************************** 
@users.route('/account')
@login_required
def account():
    user=User.query.get(current_user.id)
    return render_template('account.html',user=user)
#  ******************************** /POSTS ******************************** 
@users.route('/Posts')
@login_required
def posts():
    return render_template('posts.html')
#  ******************************** /UPDATE/{USERID} ******************************** 
@users.route('/update/<int:userid>',methods=['GET','POST'])
@login_required
def update_info(userid):
    form=UpdateInfoForm()
    user=User.query.get(current_user.id)
    if form.validate_on_submit():
        user.username=form.username.data
        user.email=form.email.data
        db.session.commit()
        flash('data updated successfully')
        return redirect(url_for('users.account'))
    elif request.method=='GET':
        form.username.data=user.username
        form.email.data=user.email
    return render_template('update.html',form=form)
#  ******************************** /LOGOUT ******************************** 
@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f"you're logged out successfully")
    return redirect(url_for('users.login'))