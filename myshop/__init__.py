from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename





app = Flask(__name__)
app.config["SECRET_KEY"]= "sathishkumar17"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



    
 
from myshop.admin import routes
from myshop.products import routes





