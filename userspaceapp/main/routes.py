# **************************************** /main/routes.py ****************************************

from flask import render_template,redirect,url_for,Blueprint
from flask_login import current_user

main=Blueprint('main',__name__)
#  ******************************** ROUTES ******************************** 
#  ******************************** / ******************************** 
@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('index.html')
