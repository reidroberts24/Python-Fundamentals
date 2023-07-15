from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class Recipe:
    DB = 'recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.is_under_30 = data['is_under_30_mins']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = []

    ############## ADD NEW RECIPE TO DB ##############
    @classmethod
    def add_rcp(cls, data):
        query = '''INSERT INTO recipes (name, instructions, description, is_under_30_mins, created_at, user_id)
                VALUES (%(name)s, %(instructions)s, %(description)s, %(is_under_30_mins)s, %(created_at)s, %(user_id)s);'''
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_rcps(cls):
        query = '''SELECT * FROM recipes
                    LEFT JOIN users on recipes.user_id = users.id;'''
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def get_rcp_by_id(cls, data):
        query = '''SELECT * FROM recipes
                    LEFT JOIN users on recipes.user_id = users.id
                    WHERE recipes.id = %(id)s;'''
        rcp = connectToMySQL(cls.DB).query_db(query, data)

        if len(rcp) < 1:
            return False
        return cls(rcp[0])
            

    @classmethod
    def edit_rcp(cls, data):
        query = '''UPDATE recipes SET 
            name = %(name)s,
            description = %(description)s,
            instructions = %(instructions)s,
            created_at = %(created_at)s, 
            is_under_30_mins = %(is_under_30_mins)s
            WHERE recipes.id = %(id)s;'''
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_rcp(cls, data):
        query = '''DELETE FROM recipes WHERE recipes.id = %(id)s;'''
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @staticmethod
    def validate_rcp(rcp):
        is_valid = True
        if not rcp['rcp_name'] or len(rcp['rcp_name']) < 3:
            flash("Must enter a recipe name with at least 3 characters!", "create")
            is_valid = False
        if not rcp['description'] or len(rcp['description']) < 3:
            flash("Must enter a recipe description with at least 3 characters!", "create")
            is_valid = False
        if not rcp['instructions'] or len(rcp['instructions']) < 3:
            flash("Must enter instructions for the recipe with at least 3 characters!", "create")
            is_valid = False
        if not rcp['date_added']:
            flash("Must enter the date the recipe was made!", "create")
            is_valid = False
        if 'under_30' not in rcp:
            flash("Must enter if recipe takes less than 30 minutes!", "create")
            is_valid = False
        return is_valid