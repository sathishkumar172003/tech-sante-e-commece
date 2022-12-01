from myshop import db, app
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False )
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount=db.Column(db.Integer, default=0 )
    description = db.Column(db.Text, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='categories', lazy=True)

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship('Brand', backref='brands', lazy=True)

    image_1 = db.Column(db.String(200), nullable=False, default="default.jpg")
    image_2 = db.Column(db.String(200), nullable=False, default="default.jpg")
    image_3 = db.Column(db.String(200), nullable=False, default="default.jpg")

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


with app.app_context():
    db.create_all()