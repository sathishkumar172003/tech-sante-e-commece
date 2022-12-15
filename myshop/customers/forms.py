from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class customer_registration_form(FlaskForm):
    username = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm password", validators=[DataRequired(), EqualTo("password")])
    profile = FileField('profile', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])  
    
    address = StringField(label="address", validators=[DataRequired()])


    country = StringField(label="Country", validators=[DataRequired()])
    state = StringField(label="state", validators=[DataRequired()])
    city = StringField(label="city", validators=[DataRequired()])

    zipcode = StringField(label='Enter zip code',validators=[DataRequired()] )
    submit = SubmitField(label="Register")



class Customer_login_form(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")

