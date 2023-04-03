from flask import render_template

from app import app
from models.order import Order
from models.orders import *



@app.route('/orders')
def index():
    return render_template('index.html', order_list = orders)

@app.route('/orders/<index>')
def read(index):
    return render_template('order.html', this_order = orders[int(index)])

