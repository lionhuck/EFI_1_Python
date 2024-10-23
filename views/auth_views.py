from flask import Blueprint,render_template, redirect, request, url_for,jsonify
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    get_jwt_identity,
    get_jwt,
    create_access_token
    )  


from forms import PaisForm
from repositories.paises_repository import PaisRepository
from services.paises_service import PaisService
from celulares import  *
from datetime import timedelta
from schemas import UsuarioSchema, MinimalUsuarioSchema

auth_bp = Blueprint('auth',__name__)

@auth_bp.route("/users", methods=['POST', 'GET'])
@jwt_required()
def user(): 
    print(get_jwt_identity())
    additional_data =get_jwt()
    administrador = additional_data.get('administrador') 
    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre')
        password = data.get('password')

        if administrador is True:

            password_hasheada = generate_password_hash(
                password,
                method='pbkdf2',
                salt_length=8
            )
            print(password_hasheada)
            try:
                nuevo_usuario = Usuario(nombre=nombre, password=password_hasheada)
                db.session.add(nuevo_usuario)
                db.session.commit()
                return jsonify({'Usuario Creado':nombre}),201    
            except:
                return jsonify({'Mensaje': 'Algo salio mal'})    
        
    if administrador:
        usuarios = Usuario.query.all()
        return  UsuarioSchema().dump(usuarios, many=True),200
    else:
        usuarios = Usuario.query.all()
        return MinimalUsuarioSchema().dump(usuarios, many=True)
                
         



@auth_bp.route("/login", methods=['POST'])
def login(): 
    data = request.authorization
    print(f"Authorization: {data}")  # Para ver el contenido completo

    if data is None:
        return jsonify({"Mensaje": "Autenticación no proporcionada"}), 401

    nombre = data.username
    password = data.password

    print(f"Usuario: {nombre}, Contraseña: {password}")

    usuario = Usuario.query.filter_by(nombre=nombre).first()

    if usuario and check_password_hash(pwhash=usuario.password, password=password):
        
        acces_token = create_access_token(
            identity=nombre,
            expires_delta=timedelta(minutes=10),
            additional_claims=dict(
                administrador=usuario.is_admin
            ),
        )
        return jsonify({"Mensaje": f"Token {acces_token}"})
    else:
        return jsonify({"Mensaje": "Usuario o contraseña incorrectos"}), 401







#-----------------------EQUIPOS!!! (Index del programa) --------------------------
@auth_bp.route('/', methods=['GET', 'POST'])
def equipos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo_id = request.form['modelo_id']
        categoria_id = request.form['categoria_id']
        costo = request.form['costo']
        nuevo_equipo = Equipo(nombre=nombre,modelo_id = modelo_id, categoria_id=categoria_id, costo=costo)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('auth.equipos'))
    
    equipos = Equipo.query.all()
    modelos = Modelo.query.all()
    categorias = Categoria.query.all()
    return render_template('equipos.html', equipos=equipos, modelos=modelos, categorias=categorias)
    
    
@auth_bp.route('/editar/<id>/equipos', methods=['GET', 'POST'])
def editar_equipos(id):
    equipo = Equipo.query.get_or_404(id)
    modelos = Modelo.query.all()
    categorias = Categoria.query.all()

    if request.method == 'POST':
        equipo.nombre = request.form['nombre']
        equipo.modelo_id = request.form['modelo_id']
        equipo.categoria_id = request.form['categoria_id']
        equipo.costo = request.form['costo']
        db.session.commit()
        return redirect(url_for('auth.equipos'))  # Redirige después de editar

    return render_template('editar_equipos.html', equipo=equipo, modelos=modelos, categorias=categorias)



#-----------------------PAISES--------------------------

@auth_bp.route("/paises", methods=['POST', 'GET'])
def paises(): 
    formulario = PaisForm()

    if request.method == 'POST':
        nombre = request.form['nombre']
        services = PaisService(PaisRepository())
        paises = services.get_all()
        services.create(nombre=nombre)    
    services = PaisService(PaisRepository())
    paises = services.get_all()
    return render_template(
        'paises.html',
        paises = paises,
        formulario = formulario)


@auth_bp.route('/editar/<id>/paises', methods=['GET', 'POST'])
def editar_paises(id):
    pais = Pais.query.get_or_404(id)
    if request.method == 'POST':
        pais.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('auth.paises'))  # Redirige después de editar

    return render_template('editar_paises.html', pais=pais)



#-----------------------MODELOS--------------------------
@auth_bp.route('/modelos', methods=['GET', 'POST'])
def modelos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fabricante_id = request.form['fabricante_id']
        nuevo_modelo = Modelo(nombre=nombre, fabricante_id=fabricante_id)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('auth.modelos'))
    
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    return render_template('modelos.html', modelos=modelos, fabricantes=fabricantes)
    
    
@auth_bp.route('/editar/<id>/modelos', methods=['GET', 'POST'])
def editar_modelo(id):
    modelo = Modelo.query.get_or_404(id)
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        modelo.nombre = request.form['nombre']
        modelo.modelo_id = request.form['fabricante_id']
        db.session.commit()
        return redirect(url_for('auth.modelos'))  # Redirige después de editar

    return render_template('editar_modelos.html', modelo=modelo, fabricantes=fabricantes)

#-----------------------CATEGORIAS--------------------------

@auth_bp.route("/categorias", methods=['POST', 'GET'])
def categorias(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_categoria = Categoria(nombre=nombre)
        db.session.add(nueva_categoria)
        db.session.commit()
    categorias_query = Categoria.query.all()
    return render_template('categorias.html',categorias = categorias_query)

@auth_bp.route('/editar/<id>/categorias', methods=['GET', 'POST'])
def editar_categorias(id):
    categoria = Categoria.query.get_or_404(id)
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('auth.categorias'))  # Redirige después de editar

    return render_template('editar_categorias.html', categoria = categoria)
    
#------------------------ACCESORIOS-----------------------
@auth_bp.route("/accesorios", methods=['POST', 'GET'])
def accesorios(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_accesorio = Accesorio(nombre=nombre)
        db.session.add(nuevo_accesorio)
        db.session.commit()
    accesorios_query = Accesorio.query.all()
    return render_template('accesorios.html',accesorios = accesorios_query)

@auth_bp.route('/editar/<id>/accesorios', methods=['GET', 'POST'])
def editar_accesorio(id):
    accesorio = Accesorio.query.get_or_404(id)
    
    if request.method == 'POST':
        accesorio.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('auth.accesorios'))  # Redirige después de editar

    return render_template('editar_accesorios.html', accesorio = accesorio)

#------------------------CARACTERISTICAS-----------------------
@auth_bp.route("/caracteristicas", methods=['POST', 'GET'])
def caracteristicas(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        nueva_caracteristica = Caracteristica(nombre=nombre,descripcion=descripcion)
        db.session.add(nueva_caracteristica)
        db.session.commit()
        return redirect(url_for('auth.caracteristicas'))  # Redirige después de editar
    caracteristicas = Caracteristica.query.all()
    return render_template('caracteristicas.html', caracteristicas = caracteristicas)

@auth_bp.route('/editar/<id>/caracteristicas', methods=['GET', 'POST'])
def editar_caracteristica(id):
    caracteristica = Caracteristica.query.get_or_404(id)
    
    if request.method == 'POST':
        caracteristica.nombre = request.form['nombre']
        caracteristica.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('auth.caracteristicas'))  # Redirige después de editar

    return render_template('editar_caracteristicas.html', caracteristica=caracteristica)

#------------------------CARACTERISTICAS-MODELOS-----------------------
@auth_bp.route('/caracteristicas_modelos', methods=['GET', 'POST'])
def caract_model():
    if request.method == 'POST':
        caracteristica_id = request.form['caracteristica_id']
        modelo_id = request.form['modelo_id']
        nuevo_caract_model = CaracteristicaModelo(modelo_id=modelo_id, caracteristica_id=caracteristica_id)
        db.session.add(nuevo_caract_model)
        db.session.commit()
        return redirect(url_for('auth.caract_model'))

    caracts_models = CaracteristicaModelo.query.all()
    caracteristicas = Caracteristica.query.all()  # Traer todas las características
    modelos = Modelo.query.all()  # Traer todos los modelos
    
    return render_template('caracteristicas_modelos.html', caracts_models=caracts_models, caracteristicas=caracteristicas, modelos=modelos)

#------------------------ACCESORIOS-MODELOS-----------------------
@auth_bp.route('/accesorios_modelos', methods=['GET', 'POST'])
def acces_model():
    if request.method == 'POST':
        accesorio_id = request.form['accesorio_id']
        modelo_id = request.form['modelo_id']
        nuevo_acces_model = AccesorioModelo(accesorio_id = accesorio_id, modelo_id = modelo_id)
        db.session.add(nuevo_acces_model)
        db.session.commit()
        return redirect(url_for('auth.acces_model'))

    acces_models = AccesorioModelo.query.all()
    accesorios = Accesorio.query.all()  # Traer todos los accesorios
    modelos = Modelo.query.all()  # Traer todos los modelos
    
    return render_template('accesorios_modelos.html', acces_models=acces_models, accesorios=accesorios, modelos=modelos)

@auth_bp.route('/editar/<id>/accesorios_modelos', methods=['GET', 'POST'])
def editar_acces_model(id):
    accesorio = AccesorioModelo.query.get_or_404(id)
    accesorios = Accesorio.query.all() 
    modelos = Modelo.query.all()
    
    if request.method == 'POST':
        accesorio.accesorio_id = request.form['accesorio_id']
        accesorio.modelo_id = request.form['modelo_id']
        db.session.commit()
        return redirect(url_for('auth.acces_model'))  # Redirige después de editar

    return render_template('editar_acces_mod.html', accesorio=accesorio, accesorios=accesorios, modelos=modelos)

#-----------------------FABRICANTES-----------------------
@auth_bp.route('/fabricantes', methods=['GET', 'POST'])
def fabricantes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        pais_id = request.form['pais_id']
        nuevo_fabricante = Fabricante(nombre=nombre, pais_id=pais_id)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('auth.fabricantes'))  # Redirige para evitar el duplicado en caso de recarga

    fabricantes = Fabricante.query.all()
    paises = Pais.query.all()
    return render_template('fabricantes.html', fabricantes=fabricantes, paises=paises)

@auth_bp.route('/editar/<id>/fabricantes', methods=['GET', 'POST'])
def editar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)
    paises = Pais.query.all()
    
    if request.method == 'POST':
        fabricante.nombre = request.form['nombre']
        fabricante.pais_id = request.form['pais_id']
        db.session.commit()
        return redirect(url_for('auth.fabricantes'))  # Redirige después de editar

    return render_template('editar_fabricantes.html', fabricante=fabricante, paises=paises)

#------------------------PROVEEDORES-----------------------
@auth_bp.route("/proveedores", methods=['POST', 'GET'])
def proveedores(): 
    if request.method == 'POST':
        nombre = request.form['nombre']
        cuit = request.form['cuit']
        nuevo_proveedor = Proveedor(nombre=nombre,cuit=cuit)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('auth.proveedores'))  # Redirige después de editar
    proveedores = Proveedor.query.all()
    return render_template('proveedores.html', proveedores = proveedores)

@auth_bp.route('/editar/<id>/proveedores', methods=['GET', 'POST'])
def editar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    
    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.cuit= request.form['cuit']
        db.session.commit()
        return redirect(url_for('auth.proveedores'))  # Redirige después de editar

    return render_template('editar_proveedores.html', proveedor=proveedor)




