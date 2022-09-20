
from crypt import methods
from flask import render_template, redirect, request
from flask_app.models.user import Users
from flask_app import app

@app.route("/users/new")
def index():
    usuarios = Users.get_all()
    return render_template("crear.html", usuarios = usuarios)
            
@app.route('/enviar', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    Users.save(data)
    return redirect('/users') 

@app.route('/users')
def mostrar_usuario():
    usuarios = Users.get_all()
    print(usuarios)
    return render_template('mostrar.html', usuarios = usuarios)

@app.route('/delete/<id>')
def borrar(id):
    data ={
        "id" : int(id)
    }
    Users.delete(data)
    return redirect('/users')

@app.route('/users/<id>')
def mostrar(id):
    data = {
        "id" : int(id)
    }
    users = Users.seleccionar(data)
    users = users[0]
    return render_template('read.html', users = users)

@app.route('/users/<id>/edit')
def editar(id):
    data = {
        "id" : int(id)
    }
    users = Users.seleccionar(data)
    users = users[0]
    return render_template('editar.html', users = users)

@app.route('/users/editar/<id>', methods=["POST"])
def editar_usuario(id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id" : int(id)
    }
    Users.edit(data)

    return redirect('/users')
