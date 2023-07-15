from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

############## ADD NEW RECIPE PAGE ##############
@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('logout')
    return render_template('new_recipe.html')

############## SHOW RECIPE ##############
@app.route('/show/recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    rcp = Recipe.get_rcp_by_id({'id':recipe_id})
    rcp_creator = User.get_user_by_id({'id':rcp.user_id})
    user = User.get_user_by_id({'id':session['user_id']})
    return render_template('show_recipe.html', rcp=rcp, user=user, posted_by=rcp_creator)

############## EDIT RECIPE ##############
@app.route('/edit/recipe/<int:recipe_id>')
def edit_rcp(recipe_id):
    if 'user_id' not in session:
        return redirect('logout')
    rcp = Recipe.get_rcp_by_id({'id':recipe_id})
    return render_template('edit_recipe.html', rcp=rcp)

@app.route('/update/recipe', methods=["POST"])
def update_rcp():
    if 'user_id' not in session:
        return redirect('logout')
    rcp_id = request.form['id']
    if not Recipe.validate_rcp(request.form):
        return redirect(f'/edit/recipe/{rcp_id}')
    is_under_30 = request.form['under_30']
    if is_under_30 == "yes":
        is_under_30 = 1
    else:
        is_under_30 = 0
    data = {
        'id': int(rcp_id),
        'name': request.form['rcp_name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'is_under_30_mins': is_under_30,
        'created_at': request.form['date_added'],
        'user_id': session['user_id']
    }
    Recipe.edit_rcp(data)
    return redirect('/dashboard')

############## ADD RECIPE ##############
@app.route('/add/recipe', methods=["POST"])
def add_rcp():
    if not Recipe.validate_rcp(request.form):
        return redirect('/new/recipe')
    is_under_30 = request.form['under_30']
    if is_under_30 == "yes":
        is_under_30 = 1
    else:
        is_under_30 = 0
    data = {
        'name': request.form['rcp_name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'is_under_30_mins': is_under_30,
        'created_at': request.form['date_added'],
        'user_id': session['user_id']
    }
    Recipe.add_rcp(data)
    return redirect('/dashboard')



############## DELETE RECIPE ##############
@app.route('/delete/recipe/<int:recipe_id>')
def delete_rcp(recipe_id):
    Recipe.delete_rcp({'id':recipe_id})
    return redirect('/dashboard')