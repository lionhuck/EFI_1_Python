from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/celulares' # chequear a donde manda la informacion con respecto a la base de datos no encontrada de celulares.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from celulares import  *


@app.route("/")
def index():
    return render_template(
        'index.html'
    )

@app.route("/celulares")
def celulares():
    return render_template(
        'celulares.html'
    )

@app.route("/paises", methods=['POST', 'GET'])
def paises(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_pais = Pais(nombre=nombre)
        db.session.add(nuevo_pais)
        db.session.commit()
    paises_query = Pais.query.all()
    return render_template('paises.html',paises = paises_query)

#-----------------------FABRICANTES-----------------------
@app.route('/fabricantes', methods=['GET', 'POST'])
def fabricantes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        pais_id = request.form['pais_id']
        nuevo_fabricante = Fabricante(nombre=nombre, pais_id=pais_id)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('fabricantes'))  # Redirige para evitar el duplicado en caso de recarga

    fabricantes = Fabricante.query.all()
    paises = Pais.query.all()
    return render_template('fabricantes.html', fabricantes=fabricantes, paises=paises)

@app.route('/editar/<id>/fabricantes', methods=['GET', 'POST'])
def editar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)
    paises = Pais.query.all()
    
    if request.method == 'POST':
        fabricante.nombre = request.form['nombre']
        fabricante.pais_id = request.form['pais_id']
        db.session.commit()
        return redirect(url_for('fabricantes'))  # Redirige después de editar

    return render_template('editar_fabricantes.html', fabricante=fabricante, paises=paises)

@app.route('/eliminar/fabricantes', methods=['POST'])
def eliminar_fabricante(id):
    fabricante = Fabricante.query.get(id)
    db.session.delete(fabricante)
    db.session.commit()
    return render_template('fabricantes.html', fabricantes=fabricantes,paises=paises)

#------------------------ACCESORIOS-----------------------
@app.route("/accesorios", methods=['POST', 'GET'])
def accesorios(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_accesorio = Accesorio(nombre=nombre)
        db.session.add(nuevo_accesorio)
        db.session.commit()
    accesorios_query = Accesorio.query.all()
    return render_template('accesorios.html',accesorios = accesorios_query)

@app.route('/editar/<id>/accesorios', methods=['GET', 'POST'])
def editar_accesorio(id):
    accesorio = Accesorio.query.get_or_404(id)
    
    if request.method == 'POST':
        accesorio.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('accesorios'))  # Redirige después de editar

    return render_template('editar_accesorios.html', accesorio = accesorio)

@app.route('/eliminar/accesorios', methods=['POST'])
def eliminar_accesorio(id):
    accesorio = accesorio.query.get_or_404(id)
    db.session.delete(accesorio)
    db.session.commit()
    return render_template('accesorios.html', accesorios = accesorio)

#------------------------ALMACENES-----------------------
@app.route("/almacenes", methods=['POST', 'GET'])
def almacenes(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_almacenes = Almacen(nombre=nombre)
        db.session.add(nuevo_almacenes)
        db.session.commit()
    almacenes_query = Almacen.query.all()
    return render_template('almacenes.html',almacenes = almacenes_query)

#------------------------CARACTERISTICAS-----------------------
@app.route("/caracteristicas", methods=['POST', 'GET'])
def caracteristicas(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        nueva_caracteristica = Caracteristica(nombre=nombre,descripcion=descripcion)
        db.session.add(nueva_caracteristica)
        db.session.commit()
        return redirect(url_for('caracteristicas'))  # Redirige después de editar
    caracteristicas = Caracteristica.query.all()
    return render_template('caracteristicas.html', caracteristicas = caracteristicas)

@app.route('/editar/<id>/caracteristicas', methods=['GET', 'POST'])
def editar_caracteristica(id):
    caracteristica = Caracteristica.query.get_or_404(id)
    
    if request.method == 'POST':
        caracteristica.nombre = request.form['nombre']
        caracteristica.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('caracteristicas'))  # Redirige después de editar

    return render_template('editar_caracteristicas.html', caracteristica=caracteristica)

@app.route('/eliminar/caracteristicas', methods=['POST'])
def eliminar_caracteristica(id):
    caracteristica = Caracteristica.query.get_or_404(id)
    db.session.delete(caracteristica)
    db.session.commit()
    return render_template('caracteristicas.html', caracteristicas = caracteristicas)
