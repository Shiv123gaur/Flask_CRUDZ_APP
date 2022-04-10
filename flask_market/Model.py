from flask_market import db

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True,nullable=False)
    username=db.Column(db.String(length=15),nullable=False,unique=True)
    email_address=db.Column(db.String(length=50),unique=True,nullable=False)
    passward_hash=db.Column(db.String(length=10),nullable=False)
    budget=db.Column(db.Integer(),default=1000)
    items=db.relationship("Item",backref='owned_user',lazy=True)
    

class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=10),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False) 
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(length=200),nullable=False,unique=True)
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))
    



def __repr__(self):
   return f"Item {self.name}"


