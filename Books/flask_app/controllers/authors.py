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
    return redirect('new/author')


@app.route('/author/favorites')
def author_favorites():
    return render_template('author_favorites.html')