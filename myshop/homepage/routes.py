from flask import render_template
from myshop import app, db
from ..products.models import Product
from myshop.carts.models import Cart
from flask_login import current_user



@app.route('/home')
def home():
    page=1
    products = Product.query.order_by(Product.price.desc()).paginate(page=page, per_page=4)
    if current_user.is_authenticated:
        carts = Cart.query.filter_by(customer_id = current_user.id).all()
    else:
        carts = []
    return render_template('homepage.html', products = products , carts = carts)