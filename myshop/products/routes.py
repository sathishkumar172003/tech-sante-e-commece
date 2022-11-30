from flask import request, redirect, render_template, url_for, flash, session
from myshop import app, db
from .models import Brand, Category
from .forms import Addproduct




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
       

   
        flash('sucessfully product added', 'success')
        return redirect(url_for('addbrand'))
    return render_template('products/addproduct.html', 
    title="Add product page", form=form, brands = brand, 
    categories = category)