
from myshop import app, db, login_manager
from datetime import datetime
from flask_login import UserMixin




@login_manager.user_loader
def user_loader(user_id):
   return customer_database.query.get(user_id)

class customer_database(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(50), nullable=False)
   email = db.Column(db.String(150), unique=True, nullable=False)
   password = db.Column(db.String(50), nullable=False)

   address = db.Column(db.Text, nullable=False)
   country = db.Column(db.String(30), nullable=False)
   state = db.Column(db.String(30), nullable=False)
   city = db.Column(db.String(20), nullable=False)

   zipcode = db.Column(db.String(30), nullable=False)

   profile = db.Column(db.String(150), default="profile.jpeg", nullable=False)
   date_created = db.Column(db.DateTime, default = datetime.utcnow)







with app.app_context():
    db.create_all()
    