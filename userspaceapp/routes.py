from userspaceapp import app,login_manager,db
from userspaceapp.forms import LoginForm,RegisterForm,UpdateInfoForm
from userspaceapp.models import User
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required,current_user

#  ******************************** ROUTES ******************************** 
#  ******************************** / ******************************** 
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('index.html')
#  ******************************** /LOGIN ******************************** 
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()

    if form.validate_on_submit():
        user=User.query.filter_by(email=form.username.data).first()
        if user and user.password==form.password.data:
            flash('login successfull')
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('incorrect username or password')
            return redirect(url_for('login'))

    return render_template('login.html',form=form)
#  ******************************** /REGISTER ******************************** 
@app.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account created successfully')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)
#  ******************************** /HOME ******************************** 
@app.route('/home')
@login_required
def home():
    users=User.query.all()
    return render_template('home.html',users=users)
#  ******************************** /ACCOUNT ******************************** 
@app.route('/account')
@login_required
def account():
    user=User.query.get(current_user.id)
    return render_template('account.html',user=user)
#  ******************************** /UPDATE/{USERID} ******************************** 
@app.route('/update/<int:userid>',methods=['GET','POST'])
@login_required
def update_info(userid):
    form=UpdateInfoForm()
    user=User.query.get(current_user.id)
    if form.validate_on_submit():
        user.username=form.username.data
        user.email=form.email.data
        db.session.commit()
        flash('data updated successfully')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=user.username
        form.email.data=user.email
    return render_template('update.html',form=form)
#  ******************************** /LOGOUT ******************************** 
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f"you're logged out successfully")
    return redirect(url_for('login'))