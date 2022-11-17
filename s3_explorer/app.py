from flask import Blueprint, redirect, url_for
from flask import render_template
from flask_login import login_required, current_user
from s3_explorer import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('auth.login'))

@login_required
@main.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)

@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



