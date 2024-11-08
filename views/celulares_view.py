from flask import Blueprint, request, make_response,jsonify
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    get_jwt_identity,
    get_jwt,
    create_access_token
    )  

from app import *
from celulares import Modelo, Categoria, Equipo
from schemas import ModeloSchema, CategoriaSchema, EquipoSchema, MinimalEquipoSchema

celulares_bp = Blueprint('celulares',__name__)

@celulares_bp.route('/modelo', methods=['GET'])
def modelo():
    modelo = Modelo.query.all()
    return ModeloSchema().dump(modelo, many=True)

@celulares_bp.route('/categoria', methods=['GET'])
def categoria():
    categoria = Categoria.query.all()
    return CategoriaSchema().dump(categoria, many=True)


@celulares_bp.route('/equipos', methods=['POST','GET'])
@jwt_required()
def equipos():
    additional_data =get_jwt()
    administrador = additional_data.get('administrador') 
    if request.method == 'POST':
        if administrador:
            data = request.get_json()
            errors = EquipoSchema().validate(data)
            if errors:
                return make_response(jsonify(errors))
            else:

                nombre = data.get('nombre')
                modelo_id = data.get('modelo_id')
                categoria_id = data.get('categoria_id')
                costo = data.get('costo')
                nuevo_equipo = Equipo(nombre=nombre,modelo_id = modelo_id, categoria_id=categoria_id, costo=costo)
                db.session.add(nuevo_equipo)
                db.session.commit()
        else:
            return {"mensaje": "No tiene permisos"}

    equipos_activos = Equipo.query.filter_by(activo=1).all()

    if administrador:
        return jsonify(EquipoSchema(many=True).dump(equipos_activos))
    else:
        return jsonify(MinimalEquipoSchema(many=True).dump(equipos_activos))

@celulares_bp.route('/editar/<int:id>/equipo', methods=['GET', 'POST'])
@jwt_required()
def editar_equipo(id):
    additional_data = get_jwt()  
    administrador = additional_data.get('administrador')
    
    equipo = Equipo.query.get_or_404(id)
    
    if request.method == 'POST':
        if administrador:
            data = request.get_json()
            errors = EquipoSchema().validate(data)
            if errors:
                return make_response(jsonify(errors)), 400
            else:
                equipo.nombre = data.get('nombre')
                equipo.costo = data.get('costo')
                db.session.commit()
                return {"mensaje": "Equipo actualizado exitosamente"}, 200 
        else:
            return {"mensaje": "No tiene permisos"}, 403  

    equipos_activos = Equipo.query.filter_by(activo=1).all()
    
    if administrador:
        return jsonify(EquipoSchema(many=True).dump(equipos_activos))
    else:
        return jsonify(MinimalEquipoSchema(many=True).dump(equipos_activos))

@celulares_bp.route('/eliminar/<id>/equipo', methods=['GET', 'POST'])
@jwt_required()
def eliminar_equipo(id):
    additional_data =get_jwt()
    administrador = additional_data.get('administrador') 
    equipo = Equipo.query.get_or_404(id)
    if request.method == 'POST':
        if administrador:
            equipo.activo = False
            db.session.commit()
        else:
            return {"mensaje": "No tiene permisos"}

    equipos_activos = Equipo.query.filter_by(activo=1).all()

    if administrador:
        return jsonify(EquipoSchema(many=True).dump(equipos_activos))
    else:
        return jsonify(MinimalEquipoSchema(many=True).dump(equipos_activos))