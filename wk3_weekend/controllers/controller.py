from flask import *
from app import app
from models.book_class import Book
from models.book_object import *

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=book_list)