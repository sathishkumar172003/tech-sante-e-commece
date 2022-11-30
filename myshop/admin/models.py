from myshop import db , app


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(250), unique=True, nullable = False)
    password = db.Column(db.String(250), nullable = False)
    profile = db.Column(db.String(20), default = "default.jpg")

    
with app.app_context():
    db.create_all()