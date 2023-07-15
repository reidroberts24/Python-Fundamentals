from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
############## MAIN PAGE FOR REGISTRATION AND LOGIN ##############
@app.route('/')
def root():
    return render_template('register_login.html')

############## USER DASHBOARD ##############
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('logout')
    data = {
        'id':session['user_id']
    }

    #add get_recipes method to display alll the posted recieps
    rcps = Recipe.get_all_rcps()
    return render_template('user_dashboard.html', user=User.get_user_by_id(data), recipes=rcps)

############## ADD USER ##############
@app.route('/add/user', methods=["POST"])
def add_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    new_user_id = User.add_user(data)
    session['user_id'] = new_user_id
    return redirect('/dashboard')

############## USER LOGIN ##############
@app.route('/login', methods=["POST"])
def login():
    user = User.get_user_by_email(request.form)
    if not user:
        flash("Invalid email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')