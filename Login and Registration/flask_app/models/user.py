from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class User:
    DB = "login_and_registration_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_user(cls, data):
        query = '''SELECT * FROM users WHERE email = %(email)s'''
        user = connectToMySQL(cls.DB).query_db(query, data)
        return cls(user[0])
    
    @classmethod
    def get_user_by_id(cls, data):
        query = '''SELECT * FROM users WHERE id = %(id)s'''
        user = connectToMySQL(cls.DB).query_db(query, data)
        return cls(user[0])
    
    @classmethod
    def save(cls, data):
        query = '''INSERT INTO users (first_name, last_name, email, password)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'''
        return connectToMySQL(cls.DB).query_db(query, data)

            
    @staticmethod
    def validate_user(user):
        is_valid = True
        name_pattern = r'^[a-zA-Z]+$'
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        query = '''SELECT email FROM users WHERE email = %(email)s;'''
        results = connectToMySQL(User.DB).query_db(query, user)

        if len(user['first_name']) < 2 or not re.match(name_pattern, user['first_name']):
            flash("First name must be longer than 2 characters and only consist of letters!", "register")
            is_valid = False

        if len(user['last_name']) < 2 or not re.match(name_pattern, user['last_name']):
            flash("Last name must be longer than 2 characters and only consist of letters!", "register")
            is_valid = False

        # must get all emails from DB
        if results:
            flash("Email already being used!", "register")
            is_valid = False

        if not re.match(email_pattern, user['email']):
            flash("Invalid email format!", "register")
            is_valid = False

        if len(user['pw']) < 8:
            flash("Invalid password!", "register")
            is_valid = False

        if user['pw'] != user['confirm_pw']:
            flash("Passwords do not match!", "register")
            is_valid = False

        return is_valid
