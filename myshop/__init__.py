from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_msearch import Search
from flask_migrate import Migrate
from flask_login import LoginManager 






app = Flask(__name__)
app.config["SECRET_KEY"]= "sathishkumar17"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

search = Search()
search.init_app(app)

migrate = Migrate(app, db,render_as_batch=True) 


with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)

    
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'customer_login'
login_manager.login_message_category = 'danger'
login_manager.login_message = 'please login to access the pages'




from myshop.admin import routes
from myshop.products import routes

from myshop.carts import routes
from myshop.customers import routes

from myshop.homepage import routes





