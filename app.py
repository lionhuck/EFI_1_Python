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



#-----------------------PAISES--------------------------

@app.route("/paises", methods=['POST', 'GET'])
def paises(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_pais = Pais(nombre=nombre)
        db.session.add(nuevo_pais)
        db.session.commit()
    paises_query = Pais.query.all()
    return render_template('paises.html',paises = paises_query)


@app.route('/editar/<id>/paises', methods=['GET', 'POST'])
def editar_paises(id):
    pais = Pais.query.get_or_404(id)
    if request.method == 'POST':
        pais.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('paises'))  # Redirige después de editar

    return render_template('editar_paises.html', paises = paises)



#-----------------------MODELOS--------------------------
@app.route('/modelos', methods=['GET', 'POST'])
def modelos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fabricante_id = request.form['fabricante_id']
        nuevo_modelo = Modelo(nombre=nombre, fabricante_id=fabricante_id)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('modelos'))
    
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    return render_template('modelos.html', modelos=modelos, fabricantes=fabricantes)
    
    
# @app.route('/editar/<id>/fabricantes', methods=['GET', 'POST'])
# def editar_fabricante(id):
#     fabricante = Fabricante.query.get_or_404(id)
#     paises = Pais.query.all()
    
#     if request.method == 'POST':
#         fabricante.nombre = request.form['nombre']
#         fabricante.pais_id = request.form['pais_id']
#         db.session.commit()
#         return redirect(url_for('fabricantes'))  # Redirige después de editar

#     return render_template('editar_fabricantes.html', fabricante=fabricante, paises=paises)

#-----------------------CATEGORIAS--------------------------

@app.route("/categorias", methods=['POST', 'GET'])
def categorias(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_categoria = Categoria(nombre=nombre)
        db.session.add(nueva_categoria)
        db.session.commit()
    categorias_query = Categoria.query.all()
    return render_template('categorias.html',categorias = categorias_query)

@app.route('/editar/<id>/categorias', methods=['GET', 'POST'])
def editar_categorias(id):
    categoria = Categoria.query.get_or_404(id)
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('categorias'))  # Redirige después de editar

    return render_template('editar_categorias.html', categorias = categorias)
    
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


@app.route('/editar/<id>/almacenes', methods=['GET', 'POST'])
def editar_almacenes(id):
    almacen = Almacen.query.get_or_404(id)
    if request.method == 'POST':
        almacen.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('almacenes'))  # Redirige después de editar

    return render_template('editar_almacenes.html', almacenes = almacenes)

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

#------------------------CARACTERISTICAS-MODELOS-----------------------
@app.route('/caracteristicas_modelos', methods=['GET', 'POST'])
def caract_model():
    if request.method == 'POST':
        caracteristica_id = request.form['caracteristica_id']
        modelo_id = request.form['modelo_id']
        nuevo_caract_model = CaracteristicaModelo(modelo_id=modelo_id, caracteristica_id=caracteristica_id)
        db.session.add(nuevo_caract_model)
        db.session.commit()
        return redirect(url_for('caract_model'))

    caracts_models = CaracteristicaModelo.query.all()
    caracteristicas = Caracteristica.query.all()  # Traer todas las características
    modelos = Modelo.query.all()  # Traer todos los modelos
    
    return render_template('caracterisitas_modelos.html', caracts_models=caracts_models, caracteristicas=caracteristicas, modelos=modelos)

#------------------------ACCESORIOS-MODELOS-----------------------
@app.route('/accesorios_modelos', methods=['GET', 'POST'])
def acces_model():
    if request.method == 'POST':
        accesorio_id = request.form['accesorio_id']
        modelo_id = request.form['modelo_id']
        nuevo_acces_model = AccesorioModelo(accesorio_id = accesorio_id, modelo_id = modelo_id)
        db.session.add(nuevo_acces_model)
        db.session.commit()
        return redirect(url_for('acces_model'))

    acces_models = AccesorioModelo.query.all()
    accesorios = Accesorio.query.all()  # Traer todos los accesorios
    modelos = Modelo.query.all()  # Traer todos los modelos
    
    return render_template('accesorios_modelos.html', acces_models=acces_models, accesorios=accesorios, modelos=modelos)

@app.route('/editar/<id>/accesorios_modelos', methods=['GET', 'POST'])
def editar_acces_model(id):
    accesorio = AccesorioModelo.query.get_or_404(id)
    accesorios = Accesorio.query.all() 
    modelos = Modelo.query.all()
    
    if request.method == 'POST':
        accesorio.accesorio_id = request.form['accesorio_id']
        accesorio.modelo_id = request.form['modelo_id']
        db.session.commit()
        return redirect(url_for('acces_model'))  # Redirige después de editar

    return render_template('editar_acces_mod.html', accesorio=accesorio, accesorios=accesorios, modelos=modelos)

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

#------------------------PROVEEDORES-----------------------
@app.route("/proveedores", methods=['POST', 'GET'])
def proveedores(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        cuit = request.form['cuit']
        nuevo_proveedor = Proveedor(nombre=nombre,cuit=cuit)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('proveedores'))  # Redirige después de editar
    proveedores = Proveedor.query.all()
    return render_template('proveedores.html', proveedores = proveedores)

@app.route('/editar/<id>/proveedores', methods=['GET', 'POST'])
def editar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    
    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.cuit= request.form['cuit']
        db.session.commit()
        return redirect(url_for('proveedores'))  # Redirige después de editar

    return render_template('editar_proveedores.html', proveedor=proveedor)

