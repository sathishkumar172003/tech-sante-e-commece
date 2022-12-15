from flask import Flask, render_template, request, redirect, url_for, session, flash
from myshop import app, db, bcrypt
from .forms import customer_registration_form
from .models import customer_database
from .forms import Customer_login_form
from werkzeug.utils import secure_filename
import uuid
import os

UPLOAD_FOLDER = '/home/sathish/VsCode/python-projects/e-commerce/myshop/static/images/user_images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.route('/customerRegister', methods=['POST','GET'])
def customer_sign_in():
    form = customer_registration_form()
    if request.method == "POST" and form.validate_on_submit():
        print('form fe') 
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
        flash(f' {username}successfully created account ', 'success')
        return redirect(url_for('product_home'))
   

        


    return render_template('customers/sign_in.html', form=form)



@app.route('/customerLogin', methods=["POST", "GET"])
def customer_login():
    form = Customer_login_form()
    
    if request.method == "POST" and form.validate_on_submit():
        customer = customer_database.query.filter_by(email = form.email.data).first()
        if customer:
            print(customer.email)
            password = bcrypt.check_password_hash(customer.password, form.password.data)
            if password:
                
                flash('succesfully logged in', 'success')
                return redirect(url_for('product_home'))
            else:
                flash('password incorrect', 'danger')
                return redirect(request.referrer)

        else:
            flash('email not found, please check your email ', 'danger')
            return redirect(url_for('customer_login'))
        
    return render_template('customers/login.html',form=form)

