from flask import Flask, render_template, request, redirect, url_for, session, flash
from myshop import app, db, bcrypt
from .forms import customer_registration_form
from .models import customer_database
from myshop.carts.models import Cart, customer_order
from .forms import Customer_login_form
from werkzeug.utils import secure_filename
import uuid
import os
from flask_login import login_required, login_user, logout_user, current_user
import secrets

from datetime import datetime

ordered_date = datetime.utcnow().day
ordered_month = datetime.utcnow().month
delivery_date = ordered_date + 5
delivery_month = 0
delivery_year = datetime.utcnow().year



months_with_31_days = [1,3,5,7,9,11,12]
months_with_30_days = [4,6,8,10]

if ordered_month in months_with_31_days:
   if ordered_date > 27:
        if delivery_date > 31:
            
            add_date =  delivery_date - 31
            delivery_date = 1
            
            for n in range(1,add_date):
                delivery_date += 1
         
        if ordered_month == 12:
            delivery_month = 1
            delivery_year += 1
        else:
            delivery_month = ordered_month + 1

if ordered_month in months_with_30_days:
   if ordered_date > 27:
        if delivery_date > 31:
            
            add_date =  delivery_date - 31
            delivery_date = 1
            print(f'add date{add_date}')
            for n in range(1,add_date):
                delivery_date += 1
         
        if ordered_month == 12:
            delivery_month = 1
        else:
            delivery_month = ordered_month + 1

@app.route('/customerHomepage', methods=['GET', "POST"])
@login_required
def customer_homepage():
    return render_template('customers/customer_homepage.html')

@app.route('/customerRegister', methods=['POST','GET'])

def customer_sign_in():
    form = customer_registration_form()
    if  form.validate_on_submit():
       
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        country = form.country.data
        state = form.state.data
        city = form.city.data
        address = form.address.data
        image_1 = request.files['profile']
        image_1_pic = secure_filename(image_1.filename)
        image_1_uuid = str(uuid.uuid1()) + "_" + image_1_pic
        profile = image_1.save(os.path.join(app.config['UPLOAD_FOLDER'], image_1_uuid))
        zipcode  = form.zipcode.data
        user = customer_database(username=username, email = email, password = password, address = address, city= city, country = country,
        profile = image_1_uuid, state = state , zipcode=zipcode)
        db.session.add(user)
        db.session.commit()
        flash(f' Welcome {username} ', 'success')
        return redirect(url_for('product_home'))
   

        


    return render_template('customers/sign_in.html', form=form, title='user registration')



@app.route('/customerLogin', methods=["POST", "GET"])

def customer_login():
    form = Customer_login_form()
    next = request.args.get('next')
    if form.validate_on_submit():
        customer = customer_database.query.filter_by(email = form.email.data).first()
        if customer:
            print(customer.email)
            password = bcrypt.check_password_hash(customer.password, form.password.data)
            if password:
                login_user(customer)
                flash('you have succesfully logged in', 'success')
                
                return redirect(url_for('home'))
            else:
                flash('password incorrect', 'danger')
                return redirect(request.referrer)

        else:
            flash('email not found, please check your email ', 'danger')
            return redirect(request.referrer)
        
    return render_template('customers/login.html',form=form,title="user login")

@app.route('/customer/logout')
@login_required
def customer_logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/customerOrder', methods=['POST', 'GET'])
@login_required
def order_route():
    customer_id = current_user.id 
    invoice = secrets.token_hex(7)
    delivery = f'{delivery_date} / {delivery_month}/ {delivery_year}'
   
    carts = Cart.query.filter_by(customer_id = customer_id).all()
    for each in carts:
        
        order = customer_order(invoice=invoice, customer_id = customer_id, 
        deliver_date = delivery, name = each.product.name, quantity =each.quantity, price = each.product.price,
        discount = each.product.discount, product_id = each.product.id)
        db.session.add(order)
        db.session.commit()
        db.session.delete(each)
        db.session.commit()
    
    orders = customer_order.query.filter_by(customer_id = current_user.id).all()
    total_price = 0

    total_discount = 0
    for cart in orders:
                total_price += int(cart.price) * int(cart.quantity)
                dis = ((cart.discount / 100) * cart.price)
                total_discount += int(dis)
      
    final_amount = int(total_price - total_discount)
    total_saving = int(total_discount + 100)    
    
    if datetime.utcnow().day == delivery_date:
        status = "your product will be delivered by today"
    elif datetime.utcnow().day > delivery_date:
        status = "your product has delivered"
    else:
        status = "pending, yet to be delivered "


    return render_template('customers/order_page.html', orders = orders , status = status, total_discount = total_discount,
    final_amount = final_amount, total_saving=total_saving, total_price = total_price)


    
