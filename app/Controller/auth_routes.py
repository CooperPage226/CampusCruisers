from __future__ import print_function
import sys
from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from .forms import LoginForm
from config import Config
from app.Model.models import User
from datetime import datetime

from app import db

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

@bp_auth.route('/login/', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if(user is None) or (user.check_password(lform.password.data) == False):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = lform.remember_me.data)
        return redirect(url_for('routes.index'))
    return render_template('login.html',title = 'Sign In', form = lform)

@bp_auth.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))