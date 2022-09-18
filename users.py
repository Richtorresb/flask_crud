# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM esquema_usuarios.users;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('esquema_usuarios').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        usuarios = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO esquema_usuarios.users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('esquema_usuarios').query_db( query, data )