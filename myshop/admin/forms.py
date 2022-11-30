from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, email_validator
from .models import User

class RegistrationForm(FlaskForm):
    username = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(label="Register")



class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")

