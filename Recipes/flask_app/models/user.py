from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = 'recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_user(cls, data):
        query = '''INSERT INTO users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'''
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_user_by_email(cls, data):
        query = '''SELECT * FROM users WHERE users.email = %(email)s'''
        user = connectToMySQL(cls.DB).query_db(query, data)
        if len(user) < 1:
            return False
        return cls(user[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = '''SELECT * FROM users WHERE users.id = %(id)s'''
        user = connectToMySQL(cls.DB).query_db(query, data)
        return cls(user[0])
    
    @classmethod
    def delete_user():
        pass

    ############## VALIDATE NEW USER REGISTRATION ##############
    @staticmethod
    def validate_registration(user):
        is_valid = True

        query_email = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.DB).query_db(query_email, user)
        if len(results) >= 1:
            flash("Email is already taken!", "register")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters!", "register")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email!", "register")
            is_valid = False
        if user['password'] != user['confirm_pw']:
            flash("Passwords don't match","register")
            is_valid = False
        return is_valid
        