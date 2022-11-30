from flask import request, redirect, render_template, url_for, flash, session
from myshop import app, db
from .models import Brand, Category, Product
from .forms import Addproduct
from werkzeug.utils import secure_filename
import os 
import uuid

UPLOAD_FOLDER = '/home/sathish/VsCode/python-projects/e-commerce/myshop/static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/product/addbrand', methods=["POST", "GET"])
def addbrand():
    if request.method == "POST":
        brand_name = request.form.get('brands')
        brand = Brand(name=brand_name)
        db.session.add(brand)
        db.session.commit()
        flash(f'The brand {brand_name} added successfully', "success")
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands="brands")


@app.route('/product/addcategory', methods=["POST", "GET"])
def addcategory():
    if request.method == "POST":
        cat_name = request.form.get('category')
        category = Category(name=cat_name)
        db.session.add(category)
        db.session.commit()
        flash(f'The category {cat_name} added successfully', "success")
        return redirect(url_for('addcategory'))
    return render_template('products/addbrand.html' )



@app.route('/product/addproduct', methods=["POST", "GET"])
def addproduct():
    form = Addproduct()
    brand = Brand.query.all()
    category = Category.query.all()
    if request.method == "POST" and form.validate_on_submit():
        # getting images
        image_1 = request.files['image_1']
        image_1_pic = secure_filename(image_1.filename)
        image_1_uuid = str(uuid.uuid1()) + "_" + image_1_pic
        image_1.save(os.path.join(app.config['UPLOAD_FOLDER'], image_1_uuid))

        image_2 = request.files['image_2']
        image_2_pic = secure_filename(image_2.filename)
        image_2_uuid = str(uuid.uuid1()) + "_" + image_2_pic
        image_2.save(os.path.join(app.config['UPLOAD_FOLDER'], image_2_uuid))

        image_3 = request.files['image_3']
        image_3_pic = secure_filename(image_3.filename)
        image_3_uuid = str(uuid.uuid1()) + "_" + image_3_pic
        image_3.save(os.path.join(app.config['UPLOAD_FOLDER'], image_3_uuid))

        # saving form data into database
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        description = form.description.data




        flash('sucessfully product added', 'success')
        return redirect(url_for('addbrand'))
    return render_template('products/addproduct.html', 
    title="Add product page", form=form, brands = brand, 
    categories = category)