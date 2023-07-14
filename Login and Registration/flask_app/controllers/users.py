from flask_app.models.user import User
from flask_app import app
from flask import Flask,render_template,redirect,request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect('/')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['pw'],)
    }
    new_user_id = User.save(data)
    session['user_id'] = new_user_id
    return redirect('welcome')

@app.route('/login', methods=["POST"])
def login():
    user = User.get_user({'email': request.form['email']})

    if not user:
        flash("Invalid email", 'login')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['pw']):
        flash("Incorrect password", 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('welcome_page.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')