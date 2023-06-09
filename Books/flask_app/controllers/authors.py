from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/')
def root():
    return redirect('new/author')

##### NEW AUTHOR TEMPLATE PAGE #####
@app.route('/new/author')
def new_author():
    all_authors = Author.get_all_auths()
    return render_template('new_author.html', auths=all_authors)

##### POST: ADD NEW AUTHOR #####
@app.route('/add/author', methods=["POST"])
def add_new_author():

    data = {
        'name': request.form['auth_name']
    }
    Author.add_author(data)
    return redirect('/')

##### AUTHOR FAVORITE PAGE #####
@app.route('/author/favorites')
def author_favorites():
    books = Book.get_all_books()
    return render_template('author_favorites.html', books=books)

@app.route('/author/favorites/<int:auth_id>')
def show_auth_favorites(auth_id):
    author = Author.get_single_auth({'id': auth_id})
    faves = author.get_auth_favorites({'id': auth_id})
    fave_ids = []
    for book in faves:
        fave_ids.append(book['id'])
    books = Book.get_all_books()
    return render_template('author_favorites.html', auth=author, all_books=books, faves=faves, fave_ids=fave_ids)

##### ADD BOOK TO AUTHOR'S FAVORITES #####
@app.route('/add/author/favorite/<int:auth_id>', methods=["POST"])
def add_author_favorite(auth_id):
    author = Author.get_single_auth({'id':auth_id})
    data = {
        'author_id': auth_id,
        'book_id': request.form['book_id']
    }
    author.add_auth_favorite(data)
    return redirect(f'/author/favorites/{auth_id}')


########### ADDED DELETE AUTHOR METHOD BUT ONLY WORKS FOR AUTHS WITHOUT
# RELATIONSHIPS TO OTHER TABLES
# DIDN'T HAVE TIME TO FINISH OUT THE FUNCTIONALITY
# STUDYING TO ACE THE EXAM

@app.route('/delete/author/<int:auth_id>', methods=["POST"])
def delete_author(auth_id):
    data = {
        'id': auth_id
    }
    Author.delete_author(data)
    return redirect('/')