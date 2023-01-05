from myshop import db, app
from myshop.products.models import Product
from myshop.customers.models import customer_database
from datetime import datetime


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    quantity = db.Column(db.Integer,  default=1)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='product', lazy=True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer_database.id'), nullable=False)
    customer = db.relationship('customer_database', backref='customer',lazy=True)

class customer_order(db.Model):
   id = db.Column(db.Integer, primary_key = True)

   invoice = db.Column(db.String(50), nullable=False)
   ordered_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

   deliver_date = db.Column(db.String(50), nullable=False)

   status = db.Column(db.String(50), default="pending")

   customer_id = db.Column(db.Integer, db.ForeignKey('customer_database.id'), nullable=False)
   customer = db.relationship('customer_database', backref="ordered_customer", lazy=True)

   quantity = db.Column(db.Integer, nullable=False, default=1)
   price = db.Column(db.Integer, nullable=False)
   discount = db.Column(db.Integer)
   name = db.Column(db.String(250), nullable=False)
   

   product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
   product = db.relationship('Product', backref='ordered_product', lazy=True)

   



with app.app_context():
    db.create_all()