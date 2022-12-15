from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_msearch import Search
from flask_migrate import Migrate






app = Flask(__name__)
app.config["SECRET_KEY"]= "sathishkumar17"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

search = Search()
search.init_app(app)

migrate = Migrate(app, db) 




    
 
from myshop.admin import routes
from myshop.products import routes

from myshop.carts import routes
from myshop.customers import routes





