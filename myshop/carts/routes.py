from flask import Flask,flash, render_template, redirect, session, url_for, request
from myshop import db, app
from myshop.products.models import Product


def merge_cart(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    else:
        return False

@app.route('/showCarts', methods=["POST", "GET"])
def show_carts():
    
    if 'shopping_cart' not in session:
        flash('you have no item in your cart', 'warning')
        return redirect(request.referrer)
    if len(session['shopping_cart']) == 0:
        return redirect(url_for('product_home'))
    total_price = 0

    total_discount = 0
    for key, product in session['shopping_cart'].items():
        total_price += int(product['quanity'] )* int(product['price'])
        dis = ((int(product['discount']) / 100 ) * product['price'])
        total_discount += int(dis)
    final_amount = int(total_price - total_discount)
    total_saving = int(total_discount + 100)
    return render_template('products/show_carts.html', total_price = total_price,
    total_discount=total_discount, total_saving=total_saving, final_amount=final_amount)


@app.route('/addCart' , methods=["POST"])
def add_cart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        product = Product.query.filter_by(id = product_id).first()
        if request.method == "POST" and quantity:
            cart_item = {
                product_id: {
                    "name":product.name,
                    'price':product.price,
                    'quanity':quantity,
                    'discount':product.discount,
                    'brand':product.brand.name,
                    'category':product.category.name,
                    'image':product.image_1
                }
            }
            if 'shopping_cart' in session:
                print(session['shopping_cart'])
                if product_id in session['shopping_cart']:
                    flash('the product is already in your cart', 'info')
                    return redirect(request.referrer)

                else:
                    session['shopping_cart'] = merge_cart(session['shopping_cart'], cart_item)
                    return redirect(request.referrer)
            else:
                session['shopping_cart'] = cart_item
                return redirect(request.referrer)
                


    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@app.route('/updateCart/<int:id>', methods=["POST","GET"])
def update_cart(id):
    if 'shopping_cart' not in session and len(session['shopping_cart']) == 0:
        return redirect(url_for('product_home'))
    if request.method == "POST":
        quantity = request.form.get('quantity')
        try:
            session.modified = True
            for key, item in session['shopping_cart'].items():
                if int(key) == int(id):
                    print(key)
                    item['quanity'] = quantity
                    print(item['quanity'])
                    return redirect(url_for('show_carts'))
        except Exception as e:
            print(e)

    return redirect(request.referrer)



@app.route('/removeCart/<int:id>')
def remove_cart(id):
    if 'shopping_cart' not in session and len(session['shopping_cart']):
        return redirect(url_for('product_home'))
    
    try:
        session.modified = True
        for key, item in session['shopping_cart'].items():
            if int(key) == int(id):
                
                session['shopping_cart'].pop(key, None)
                print('succesffully delted')
                return redirect(url_for('show_carts'))
    except Exception as e:
        print(e)
    
    return redirect(request.referrer)



@app.route('/clearCart')
def clear_cart():
    try:
        session.pop('shopping_cart')
        return redirect(url_for('product_home'))
    except Exception as e:
        print(e)
    return redirect(url_for('product_home'))

  