from flask_market import db

class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=10),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False) 
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(length=200),nullable=False,unique=True)
    

