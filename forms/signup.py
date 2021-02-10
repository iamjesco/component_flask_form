from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class SignUp(FlaskForm):
	username = StringField('Username', [DataRequired(), Length(min=2, max=25)])
	email = StringField('Email', [DataRequired(), Email()])
	password = PasswordField('Password', [DataRequired(), Length(min=8, max=25)])