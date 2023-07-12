from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
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
            auths.append(cls(auth))
        return auths

    ##### GET SINGLE AUTHOR #####
    @classmethod
    def get_single_auth(cls, data):
        query = '''SELECT * FROM authors WHERE authors.id = %(id)s'''
        auth_from_db = connectToMySQL('books_schema').query_db(query, data)
        return cls(auth_from_db[0])
    
    ##### ADD AUTHOR'S FAVORITE #####
    @classmethod
    def add_auth_favorite(cls, data):
        query = '''INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);
                '''
        return connectToMySQL('books_schema').query_db(query, data)
        
    ##### GET AUTHOR'S FAVORITE BOOKS #####
    @classmethod
    def get_auth_favorites(self, data):
        query = '''
                SELECT * FROM books
                LEFT JOIN favorites ON favorites.book_id = books.id
                LEFT JOIN authors ON favorites.author_id = authors.id
                WHERE authors.id = %(id)s;
                '''
        results = connectToMySQL('books_schema').query_db(query, data)
        favorites = []
        for book in results:
            favorites.append(book)
        return favorites


    ##### ADD AUTHOR #####
    @classmethod
    def add_author(cls, data):
        query = '''
            INSERT INTO authors (name, created_at, updated_at)
            VALUES (%(name)s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());'''
        return connectToMySQL('books_schema').query_db(query, data)
    
    ##### ADD AUTHOR #####
    @classmethod
    def delete_author(cls, data):
        query = '''DELETE FROM authors 
                    WHERE authors.id = %(id)s;'''
        return connectToMySQL('books_schema').query_db(query, data)