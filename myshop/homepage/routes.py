from flask import render_template
from myshop import app, db
from ..products.models import Product



@app.route('/home')
def home():
    page=1
    products = Product.query.paginate(page=page, per_page=4)
    return render_template('homepage.html', products = products )