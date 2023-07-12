from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

##### ADD BOOK #####
@app.route('/new/book')
def new_book():
    all_books = Book.get_all_books()
    return render_template('new_book.html', books=all_books)

##### BOOK'S FAVORITED PAGE #####
@app.route('/book/favorites')
def book_favorites():
    return render_template('book_favorites.html')

##### ADD BOOK #####
@app.route('/add/book', methods=["POST"])
def add_booK():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    
    book_id = Book.add_book(data)
    return redirect(f'/book/favorites/{book_id}')

##### SHOW PAGE WITH THE AUTHORS WHO FAVED THE BOOK #####
@app.route('/book/favorites/<int:book_id>')
def show_book_favorites(book_id):
    authors_who_favorited = Book.get_book_favorites({'id': book_id})
    auth_ids = []
    for auth in authors_who_favorited:
        auth_ids.append(auth['id'])
    all_authors = Author.get_all_auths()
    book = Book.get_single_book(book_id)
    return render_template('book_favorites.html', book=book, all_auths=all_authors, auths_who_faved=authors_who_favorited, auth_ids=auth_ids)

##### ADD AN AUTHOR WHO FAVORITED THE BOOK #####
@app.route('/add/book/favorite/<int:book_id>', methods=["POST"])
def add_book_fave(book_id):
    data = {
        'author_id': request.form['auth_id'],
        'book_id': book_id
    }
    Book.add_book_fave(data)
    return redirect(f'/book/favorites/{book_id}')


# WOULD'VE ADDED METHOD TO REMOVE BOOKS FROM AUTHOR'S
# FAVORITED LIST BUT WOULD TAKE TOO LONG
# NEED TO STUDY FOR BELT