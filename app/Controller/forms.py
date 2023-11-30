from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, IntegerField, BooleanField
from wtforms.validators import  DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from flask_ckeditor import CKEditorField