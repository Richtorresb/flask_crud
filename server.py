from flask import Flask, render_template, redirect, request

from users import Users

app = Flask(__name__)
@app.route("/users/new")
def index():
    # llamar al método de clase get all para obtener todos los usuarios
    usuarios = Users.get_all()
    print(usuarios)
    return render_template("leer.html", usuarios = usuarios)
            
@app.route('/enviar', methods=["POST"])
def create_user():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Users
    Users.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/users') 

@app.route('/users')
def mostrar_usuario():
    usuarios = Users.get_all()
    return render_template('crear.html', usuarios = usuarios)



if __name__ == "__main__":
    app.run(debug=True)

