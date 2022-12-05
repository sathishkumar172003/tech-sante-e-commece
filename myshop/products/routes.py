from flask import request, redirect, render_template, url_for, flash, session, current_app
from myshop import app, db
from .models import Brand, Category, Product
from .forms import Addproduct
from werkzeug.utils import secure_filename
import os 
import uuid

UPLOAD_FOLDER = '/home/sathish/VsCode/python-projects/e-commerce/myshop/static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.route('/')
def home():
    product = Product.query.filter(Product.stock > 0)
    brands = Brand.query.all()
    categories = Category.query.all()
    return render_template('products/all_products_page.html', products = product,
    brands=brands,categories=categories )


@app.route('/product/addbrand', methods=["POST", "GET"])
def addbrand():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        brand_name = request.form.get('brands')
        brands = Brand.query.filter_by(name=brand_name).first()

        try:
            
            brand = Brand(name=brand_name)
            db.session.add(brand)
            db.session.commit()
            flash(f'The brand {brand_name} added successfully', "success")
            return redirect(url_for('addbrand'))
        except:
            if brands:
                flash(f"{brand_name} is already added", "warning")
                return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands="brands",bg_dark = "true")


@app.route('/product/updatebrand/<int:id>' ,methods=["POST","GET"])
def updatebrand(id):
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    if request.method == "POST":
        brand_name = request.form.get('brands')
        updatebrand.name = brand_name
        db.session.commit()
        flash("brand updated sucesfully ", "success")
        return redirect(url_for('brands'))

    return render_template('products/update_brand.html', title="Update Brand" ,brands="brands",
     updatebrand=updatebrand, bg_dark = "true")


@app.route('/product/deletebrand/<int:id>', methods = ["POST", "GET"])
def deletebrand(id):
    if "email" not in session:
        flash("please login to access this page", "danger")
        return redirect(url_for('login'))
    deletebrand = Brand.query.get_or_404(id)
    if deletebrand:
        brand_name = deletebrand.name;
        try:

            db.session.delete(deletebrand)
            db.session.commit()
            flash(f"{brand_name} deleted successfully", "success")
            return redirect(url_for('brands'))
        except:
            flash(f"{brand_name} can't be deleted because the product associated with this brand is available in the market", "danger")
            return redirect(url_for('brands'))
 


@app.route('/product/addcategory', methods=["POST", "GET"])
def addcategory():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        cat_name = request.form.get('category')
        categories = Category.query.filter_by(name=cat_name)
        try:
            category = Category(name=cat_name)
            db.session.add(category)
            db.session.commit()
            flash(f'The category {cat_name} added successfully', "success")
            return redirect(url_for('addcategory'))
        except:
            if categories:
                flash(f'The {cat_name} is already available', 'warning')
                return redirect(url_for('addcategory'))

    return render_template('products/addbrand.html' , bg_dark = "true")

@app.route('/product/updatecat/<int:id>' ,methods=["POST","GET"])
def updatecat(id):
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    if request.method == "POST":
        cat_name = request.form.get('category')
        updatecat.name = cat_name
        db.session.commit()
        flash("category updated sucesfully ", "success")
        return redirect(url_for('category'))

    return render_template('products/update_brand.html', title="Update Brand" ,
     updatecat=updatecat, bg_dark = "true")


@app.route('/product/deletecat/<int:id>')
def deletecat(id):
    if "email" not in session:
        flash("login to access this page", "danger")
        return redirect(url_for('login'))
    category = Category.query.get_or_404(id)
    if category:
        cat_name = category.name
        try:
            db.session.delete(category)
            db.session.commit()
            flash(f"{cat_name} successfully deleted", "success")
            return redirect(url_for('category'))
        except :
            flash(f"{cat_name} can't be deleted because the product associated with this  category is  available in the market", "danger")
            return redirect(url_for('category'))

    


@app.route('/product/addproduct', methods=["POST", "GET"])
def addproduct():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    form = Addproduct()
    brand = Brand.query.all()
    category = Category.query.all()
    if request.method == "POST" and form.validate_on_submit():
        # getting images
        image_1 = request.files['image_1']
        image_1_pic = secure_filename(image_1.filename)
        image_1_uuid = str(uuid.uuid1()) + "_" + image_1_pic
        image_1 = image_1.save(os.path.join(app.config['UPLOAD_FOLDER'], image_1_uuid))

        image_2 = request.files['image_2']
        image_2_pic = secure_filename(image_2.filename)
        image_2_uuid = str(uuid.uuid1()) + "_" + image_2_pic
        image_2 = image_2.save(os.path.join(app.config['UPLOAD_FOLDER'], image_2_uuid))


        image_3 = request.files['image_3']
        image_3_pic = secure_filename(image_3.filename)
        image_3_uuid = str(uuid.uuid1()) + "_" + image_3_pic
        image_3 = image_3.save(os.path.join(app.config['UPLOAD_FOLDER'], image_3_uuid))

        # saving form data into database
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        description = form.description.data
        brand_id = request.form.get('brand')
        category_id = request.form.get('category')

        product_1 = Product(name = name, price = price, discount = discount,
        description = description, stock = stock, image_1 = image_1_uuid, image_2=image_2_uuid,
        image_3= image_3_uuid, brand_id = brand_id, category_id = category_id)

        db.session.add(product_1)
        db.session.commit()

        flash(f'The  product {name} added to your database', 'success')
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', 
    title="Add product page", form=form, brands = brand, 
    categories = category, bg_dark = "true")


@app.route('/product/updatepro/<int:id>', methods=["POST", "GET"])
def updatepro(id):
    if "email" not in session:
        flash("login to access this page", "danger")
        return redirect(url_for('login'))
    form = Addproduct()
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Product.query.get_or_404(id)
    if form.validate_on_submit() and request.method == "POST":
        
        product.price = form.price.data
        product.name = form.name.data
        product.stock = form.stock.data
        product.description = form.description.data
        product.discount = form.discount.data

        image_1 = request.files['image_1']
        image_1_pic = secure_filename(image_1.filename)
        image_1_uuid = str(uuid.uuid1()) + "_" + image_1_pic
        image_1 = image_1.save(os.path.join(app.config['UPLOAD_FOLDER'], image_1_uuid))
        try:
            os.unlink(os.path.join(current_app.root_path, 'static/images/' + product.image_1))
            product.image_1 = image_1_uuid
        except:
            product.image_1 = image_1_uuid

        image_2 = request.files['image_2']
        image_2_pic = secure_filename(image_2.filename)
        image_2_uuid = str(uuid.uuid1()) + "_" + image_2_pic
        image_2 = image_2.save(os.path.join(app.config['UPLOAD_FOLDER'], image_2_uuid))
        
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            product.image_2 = image_2_uuid
        except:
            product.image_2 = image_2_uuid

        image_3 = request.files['image_3']
        image_3_pic = secure_filename(image_3.filename)
        image_3_uuid = str(uuid.uuid1()) + "_" + image_3_pic
        image_3 = image_3.save(os.path.join(app.config['UPLOAD_FOLDER'], image_3_uuid))
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
            product.image_3 = image_3_uuid
        except:
            product.image_3 = image_3_uuid

        db.session.commit()
        flash('product updated scuccesfully', 'success')
        return redirect(url_for('products'))

    elif request.method == "GET":
        form.name.data = product.name
        form.price.data = product.price
        form.stock.data = product.stock
        form.description.data = product.description
        form.discount.data = product.discount
        
        form.image_1.data = product.image_1
        form.image_2.data = product.image_2
        form.image_3.data = product.image_3
 
    return render_template('products/update_product.html', brands = brands,
    categories = categories, form = form, bg_dark='true', product = product, title="Update page")




@app.route('/product/deleteproduct/<int:id>', methods=["GET"])
def deleteproduct(id):
    product = Product.query.get_or_404(id)
    product_name = product.name
    try:
        os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
        os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
        os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        db.session.delete(product)
        db.session.commit()
        flash(f'{product_name} have succesfully deleted', 'success')
        return redirect(url_for('products'))
    except:
        flash(f" product {product_name} can't be deleted", "danger")
        return redirect(url_for('products'))


    