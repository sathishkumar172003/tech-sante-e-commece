from flask import Flask,flash, render_template, redirect, session, url_for, request, abort
from myshop import db, app
from myshop.products.models import Product
from flask_login import current_user, login_required
from .models import Cart




@app.route('/showCarts', methods=["POST", "GET"])
@login_required
def show_carts():
    cart_list = Cart.query.filter_by(customer_id = current_user.id).all()
    if len(cart_list) == 0:
        flash('you have no item in your cart', 'warning')
        return redirect(url_for('product_home'))
    else:
        if current_user.is_authenticated:
            carts = Cart.query.filter_by(customer_id = current_user.id).all()
            total_price = 0

            total_discount = 0
            for cart in carts:
                total_price += int(cart.product.price) * int(cart.quantity)
                dis = ((cart.product.discount / 100) * cart.product.price)
                total_discount += int(dis)
            # for key, product in session['shopping_cart'].items():
            #     total_price += int(product['quanity'] )* int(product['price'])
            #     dis = ((int(product['discount']) / 100 ) * product['price'])
            #     total_discount += int(dis)
            final_amount = int(total_price - total_discount)
            total_saving = int(total_discount + 100)
            return render_template('products/show_carts.html', total_price = total_price,
            total_discount=total_discount, total_saving=total_saving, final_amount=final_amount, carts = carts)

      
            
@app.route('/addCart' , methods=["POST", "GET"])
@login_required
def add_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    customer_id = current_user.id
    product = Product.query.filter_by(id = product_id).first()
    if request.method == "POST" and quantity:
      
        try:
           
            cart = Cart.query.filter_by(product_id = product_id).first()
            if cart:

                if cart.customer_id == current_user.id:
                    flash(f'{cart.product.name}  is already in your cart', 'warning')
                    return redirect(request.referrer)
            else:
                cart = Cart(product_id = product_id, customer_id = current_user.id)
                db.session.add(cart)
                db.session.commit()
                flash(f'{product.name} added to your cart ', 'success')
                return redirect(request.referrer)

        except Exception as e:
            
            print(e)
        

    
        
    
        

    
    
        
    
            

@app.route('/updateCart/<int:id>', methods=["POST","GET"])
@login_required
def update_cart(id):
    cart_list = Cart.query.filter_by(customer_id = current_user.id).all()
    if len(cart_list) == 0:
        flash('you have no item in your cart', 'warning')
        return redirect(url_for('product_home'))
    if request.method == "POST":
        quantity = request.form.get('quantity')
        try:
            cart = Cart.query.filter_by(id = id).first()
            if cart:
                cart.quantity = quantity
                db.session.commit()
                flash('updated succesfully', 'success')
                return redirect(url_for('show_carts'))
 
        except Exception as e:
            print(e)

    return redirect(request.referrer)



@app.route('/removeCart/<int:id>')
@login_required
def remove_cart(id):
    cart_list = Cart.query.filter_by(customer_id = current_user.id).all()
    if len(cart_list) == 0:
        flash('you have no item in your cart', 'warning')
        return redirect(url_for('product_home'))
    
    try:
        cart = Cart.query.get(id)
        product_name = cart.product.name
     
        db.session.delete(cart)
        db.session.commit()
        flash(f'{product_name} has deleted successfully', "success")
        return redirect(url_for('show_carts'))
    except Exception as e:
        print(e)
    
    return redirect(request.referrer)



@app.route('/clearCart')
@login_required
def clear_cart():
    if current_user.is_authenticated:
        carts = Cart.query.filter_by(customer_id = current_user.id).all()
        for cart in carts:
            db.session.delete(cart)
            db.session.commit()
        return redirect(url_for('product_home'))


  