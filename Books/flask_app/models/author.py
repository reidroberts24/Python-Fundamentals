from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data)
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    

    ##### GET ALL AUTHORS #####
    @classmethod
    def get_all_auths(cls):
        query ='''SELECT * FROM authors;'''
        authors_from_db = connectToMySQL('books_schema').query_db(query)
        auths = []
        for auth in authors_from_db:
            auths.append(auth)
        return auths

    ##### GET SINGLE AUTHOR #####
    @classmethod
    def get_single_auth(cls, auth_id):
        query = '''SELECT * FROM authors WHERE authors.id = %(id)s'''
        auth_from_db = connectToMySQL('books_schema').query_db(query, {'id': auth_id})
        return cls(auth_from_db[0])
    
    ##### GET AUTHOR'S BOOKS #####

    ##### GET AUTHOR'S FAVORITE BOOKS #####

    ##### ADD AUTHOR #####
    @classmethod
    def add_author(cls, data)
        query = '''
            INSERT INTO authors (name, created_at, updated_at)
            VALUES (%(name)s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());'''
        return connectToMySQL('books_schema').query_db(query, data)