from flask import render_template, session,flash,  request, url_for, redirect
from .. import app,db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User



@app.route("/admin")
def admin():
    if 'email' not in session:
        flash("login to access the page", 'danger')
        return redirect(url_for('login'))
    return render_template("admin/homepage.html", title="Admin Page")


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

    return render_template("admin/register.html", form = form , title="Register")

@app.route("/admin/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user :
            if bcrypt.check_password_hash(user.password, form.password.data):
                session['email'] = form.email.data
                flash(f"welcome {form.email.data}you have succesfully logged in ", "success")
                return redirect(request.args.get('next') or url_for('admin'))
            else:
                flash("password was incorrect , please try again","danger")
        else:
            flash("account not found , please create new", "danger")
            

 
    return render_template("admin/login.html", form=form, title="Login")

    