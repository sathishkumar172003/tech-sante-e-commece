from myshop import app, db, login_manager
from datetime import datetime
from flask_login import UserMixin
from datetime import datetime

import json
from sqlalchemy import TypeDecorator  

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



class JsonEncodedDict(db.TypeDecorator):
   impl = db.Text

   def process_bind_param(self, value, dialect):
      if value is None:
         return {}
      else:
         json.dumps(value)
   def process_result_value(self, value, dialect):
      if value is None:
         return {}
      else:
         return json.loads(value)


class Customer_order(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   invoice = db.Column(db.String(50), unique=True, nullable=False)
   status = db.Column(db.String(50), default="pending", nullable=False)
   customer_id = db.Column(db.Integer, nullable=False, unique=False)
   
   order_date = db.Column(db.DateTime, default=datetime.utcnow)




with app.app_context():
    db.create_all()
    