from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from config import Config
#from app.Model.models import User, Student, Faculty
from datetime import datetime

from app import db

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 