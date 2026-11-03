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

@app.route("/menu/agregar", methods=('GET', 'POST'))
def agregar():
    if request.method == 'POST':
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)
        id = request.form['id']
        foto = request.form['url_foto']
        nombre = request.form['nombre']
        tipo_1 = request.form['tipo_1']
        tipo_2 = request.form['tipo_2']
        if tipo_2 == '':
            cursor.execute(f'INSERT INTO pokemons (id, nombre, tipo_1, foto) VALUES ({id}, "{nombre}", "{tipo_1}", "{foto}")')
        else:
            cursor.execute(f'INSERT INTO pokemons (id, nombre, tipo_1, tipo_2, foto) VALUES ({id}, "{nombre}", "{tipo_1}", "{tipo_2}", "{foto}")')
        conexion.commit()
        conexion.close()
        return redirect(url_for('menu'))
    return render_template('agregar.html')

@app.route('/menu/modificar=<id>', methods=('GET', 'POST'))
def modificar(id):
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemons")
    pokemons = cursor.fetchall()
    cursor.execute(f'SELECT * FROM pokemons WHERE id = {id}')
    pokemon = cursor.fetchone()
    if request.method == "POST":
        foto = request.form['url_foto']
        nombre = request.form['nombre']
        tipo_1 = request.form['tipo_1']
        tipo_2 = request.form['tipo_2']
        if tipo_2 == '':
            cursor.execute(f'UPDATE pokemons SET nombre="{nombre}", tipo_1 = "{tipo_1}", tipo_2 = NULL, foto = "{foto}" WHERE id={id}')
        else:
            cursor.execute(f'UPDATE pokemons SET nombre="{nombre}", tipo_1 = "{tipo_1}", tipo_2 = "{tipo_2}", foto = "{foto}" WHERE id={id}')
        conexion.commit()
        conexion.close()
        return redirect(url_for('modificar', id = id))
    conexion.close()
    return render_template('modificar.html', pokemon = pokemon, pokemons = pokemons)

@app.route("/menu/eliminar=<id>", methods=('GET', 'POST'))
def eliminar(id):
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM pokemons WHERE id = {id}")
    pokemon = cursor.fetchone()
    if request.method == 'POST':
        cursor.execute(f"DELETE FROM pokemons WHERE id = {id}")
        conexion.commit()
        conexion.close()
        return redirect(url_for('menu'))
    conexion.close()
    return render_template('eliminar.html', pokemon = pokemon)

@app.route("/menu/selected=<id>", methods=('GET', 'POST'))
def seleccionado(id):
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemons")
    pokemons = cursor.fetchall()

    cursor.execute(f"SELECT * FROM pokemons WHERE id = {id}")
    pokemon = cursor.fetchone()
    conexion.close()
    return render_template('selected.html', pokemon = pokemon, pokemons = pokemons)