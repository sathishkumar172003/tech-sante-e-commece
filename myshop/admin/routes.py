from flask import render_template, session,flash,  request, url_for, redirect
from .. import app,db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from myshop.products.models import Product, Brand, Category
from myshop.customers.models import customer_database




@app.route("/admin")
def admin():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    product_1 = Product.query.all()

    return render_template("admin/homepage.html", title="Admin Page",
    products = product_1, bg_dark = "true")


@app.route("/admin/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
            username = form.username.data
      
            email = form.email.data
            password = bcrypt.generate_password_hash(form.password.data)
            def checking_user():
                user = User.query.filter_by(email=form.email.data).first()
                if user:
                    return False
                else:
                    return True
            
            if checking_user():
                user = User(username = username, 
                email = email, 
                password=password)
                

                db.session.add(user)
                db.session.commit()
            
                flash("Succesfully registered", "success")
                return redirect(url_for('admin'))
            else:
                flash("email is already taken", "danger")
                return redirect(url_for('register'))

    return render_template("admin/register.html", form = form ,bg_dark = "true",  title="Register")

@app.route("/admin/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user :
            if bcrypt.check_password_hash(user.password, form.password.data):
                session['email'] = form.email.data
                flash(f"welcome {form.email.data} you have succesfully logged in ", "success")
                return redirect(request.args.get('next') or url_for('admin'))
            else:
                flash("password was incorrect , please try again","danger")
        else:
            flash("account not found ", "danger")
            

 
    return render_template("admin/login.html", form=form,bg_dark = "true",  title="Login")

    
@app.route('/admin/brands')
def brands():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/show_brands.html', title="Brand page",bg_dark = "true",  brands = brands, table_heading = "BRANDS")


@app.route('/admin/cat')
def category():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/show_brands.html', title="Category page",bg_dark = "true",  categories=categories,  table_heading = "CATEGORY")


@app.route('/admin/product')
def products():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    product_1 = Product.query.all()

    return render_template("admin/show_product.html", title="product Page",
    products = product_1, bg_dark = "true")


@app.route('/admin/customers')
def customer():
    if 'email' not in session:
        flash('login to access this page', 'danger')
        return redirect(url_for('login'))
    customer_1 = customer_database.query.all()

    return render_template('admin/show_customer.html', title='customers list', 
    customers = customer_1, bg_dark='true')
