from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length,Email
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, IntegerField, DateField, FloatField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
#from app.Model.models import User, Student, Faculty, Research_field, Language;
from wtforms.widgets import ListWidget, CheckboxInput