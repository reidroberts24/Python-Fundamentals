from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/new/book')
def new_book():
    return render_template('new_book.html')

@app.route('/book/favorites')
def book_favorites():
    return render_template('book_favorites.html')