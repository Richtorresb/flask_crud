
from mysqlconnection import connectToMySQL

class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM esquema_usuarios.users;"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        usuarios = []

        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO esquema_usuarios.users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"

        return connectToMySQL('esquema_usuarios').query_db( query, data )
    
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM esquema_usuarios.users WHERE ( users.id = %(id)s) ;"

        return connectToMySQL('esquema_usuarios').query_db( query, data )
    
    @classmethod
    def seleccionar(cls, data ):
        query = "SELECT * FROM esquema_usuarios.users WHERE ( users.id = %(id)s) ;"

        return connectToMySQL('esquema_usuarios').query_db( query, data )
    
    @classmethod
    def edit(cls, data ):
        query = "UPDATE esquema_usuarios.users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE ( users.id = %(id)s) ;"

        return connectToMySQL('esquema_usuarios').query_db( query, data )