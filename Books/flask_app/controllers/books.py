from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/new/book')
def new_book():
    all_books = Book.get_all_books()
    return render_template('new_book.html', books=all_books)

@app.route('/book/favorites')
def book_favorites():
    return render_template('book_favorites.html')

@app.route('/add/book', methods=["POST"])
def add_booK():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.add_book(data)
    return redirect('/new/book')


@app.route('/book/favorites/<int:book_id>')
def show_book_favorites(book_id):
    author = Book.get_book_favorites({'id': book_id})
    return render_template('book_favorites.html')
