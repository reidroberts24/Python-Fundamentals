from flask import Flask, render_template, redirect, session, request
from flask_app import app


@app.route('/new/book')
def new_author():
    return render_template('new_book.html')