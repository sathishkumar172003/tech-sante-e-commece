from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class Addproduct(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    price = IntegerField(label="Price", validators=[DataRequired()])
    discount = IntegerField(label="Discount", default=0)
    stock = IntegerField(label="Stock available", validators=[DataRequired()])

    image_1 = FileField('image-1', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    image_2 = FileField('image-2', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    
    image_3 = FileField('image-3', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png','jpeg'], 'Images only!')
    ])
    description = TextAreaField(label="Description", validators=[DataRequired()]) 
    submit = SubmitField(label="Add product")