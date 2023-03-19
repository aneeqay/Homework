from flask import *

from app import app
from models.book_class import Book
from models.book_object import *

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/books")
def books_index():
    return render_template("books/index.html", title="Catalogue", books=book_list)


@app.route("/books/<index>")
def books_show(index):
    book = book_list[int(index)]
    return render_template("books/show.html", book=book, index=index)


@app.route("/books/new")
def books_new():
    return render_template("books/new.html")


@app.route("/books", methods=["POST"])
def books_create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    link = request.form["link"]
    image = request.form["image"]
    new_book = Book(title, author, genre, link, image)
    add_book(new_book)
    return redirect("/books")


@app.route("/books/delete/<index>", methods=["POST"])
def books_delete(index):
    delete_book(int(index))
    return redirect("/books")


# @app.route("/books/<index>", methods=["POST"])
# def books_update(index):
#     book = book_list[int(index)]
#     checked_out = "checked_out" in request.form
#     book.toggle_check_out(checked_out)
#     return redirect("/books/" + index)