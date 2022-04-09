from flask_market import app
from flask import render_template
from flask_market.Model import Item


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/market')
def market():
    items=Item.query.all()
    return render_template("market.html",items=items)