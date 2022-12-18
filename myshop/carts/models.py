from myshop import db, app
from myshop.products.models import Product
from myshop.customers.models import customer_database


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    quantity = db.Column(db.Integer,  default=1)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='product', lazy=True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer_database.id'), nullable=False)
    customer = db.relationship('customer_database', backref='customer',lazy=True)



with app.app_context():
    db.create_all()