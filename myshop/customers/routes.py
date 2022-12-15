from flask import Flask, render_template, request, redirect, url_for, session, flash
from myshop import app, db, bcrypt
from .forms import customer_registration_form
from .models import customer_registration_table
from werkzeug.utils import secure_filename
import uuid
import os

UPLOAD_FOLDER = '/home/sathish/VsCode/python-projects/e-commerce/myshop/static/images/user_images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.route('/customerRegister', methods=['POST','GET'])
def sign_in():
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
        user = customer_registration_table(username=username, email = email, password = password, address = address, city= city, country = country,
        profile = image_1_uuid, state = state , zipcode=zipcode)
        db.session.add(user)
        db.session.commit()
        flash(f' {username}successfully created account ', 'success')
        return redirect(url_for('product_home'))
   

        


    return render_template('customers/sign_in.html', form=form)