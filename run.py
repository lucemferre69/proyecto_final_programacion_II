from flask import Flask, render_template, request, redirect, url_for, flash
from conectar_db import conectar_db  

app = Flask(__name__) #esta variable tiene el valor del main cuando iniciemos

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/menu", methods=('GET','POST'))
def menu():
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('SELECT * FROM pokemons')
    pokemons = cursor.fetchall()
    conexion.close()
    return render_template('menu.html', pokemons = pokemons)

@app.route("/agregar")
def agregar():
    return render_template('agregar.html')

@app.route('/modificar/<id>', methods=('GET', 'POST'))
def modificar(id):
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM pokemons WHERE id = {id}')
    pokemon = cursor.fetchone()
    if request.method == "POST":
        foto = request.form['url_foto']
        nombre = request.form['nombre']
        tipo_1 = request.form['tipo_1']
        tipo_2 = request.form['tipo_2']
        if tipo_2 == '':
            cursor.execute(f'UPDATE pokemons SET nombre="{nombre}", tipo_1 = "{tipo_1}", tipo_2 = NULL WHERE id={id}')
        else:
            cursor.execute(f'UPDATE pokemons SET nombre="{nombre}", tipo_1 = "{tipo_1}", tipo_2 = "{tipo_2}" WHERE id={id}')
        conexion.commit()
        conexion.close()
        return redirect(url_for('modificar', id = id))
    conexion.close()
    return render_template('modificar.html', pokemon = pokemon)

@app.route("/eliminar")
def eliminar():
    return render_template('eliminar.html')