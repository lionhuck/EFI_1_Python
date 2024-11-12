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

@celulares_bp.route('/equipos/<int:id>', methods=['PUT'])
@jwt_required()
def editar_equipo(id):
    # Obtener información del token
    additional_data = get_jwt()  
    administrador = additional_data.get('administrador')
    
    # Verificar si es administrador
    if not administrador:
        return jsonify({'mensaje': 'No tiene permisos para actualizar equipos'}), 403
    
    # Buscar el equipo por ID
    equipo = Equipo.query.get(id)
    if not equipo:
        return jsonify({'mensaje': 'Equipo no encontrado'}), 404
        
    # Obtener datos de la solicitud
    data = request.get_json()
    
    try:
        if 'nombre' in data:
            equipo.nombre = data['nombre']
        
        if 'costo' in data:
            equipo.costo = data['costo']
    
        # Guardar cambios en la base de datos
        db.session.commit()
    
        return jsonify({
                'mensaje': 'Equipo actualizado exitosamente',
                'equipo': EquipoSchema().dump(equipo)
            }), 200
        
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'mensaje': f'Error al actualizar equipo: {str(e)}'}), 500


@celulares_bp.route('/equipos/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_equipo(id):
    additional_data =get_jwt()
    administrador = additional_data.get('administrador') 
    # Verificar si es administrador
    if not administrador:
        return jsonify({
            'mensaje': 'No tiene permisos para eliminar equipos'
        }), 403
    equipo = Equipo.query.get_or_404(id)
    if not equipo:
        return jsonify({
            'mensaje': 'Equipo no encontrado'
        }), 404
        
    try:
        db.session.delete(equipo)
        db.session.commit()
        
        return jsonify({
            'mensaje': 'Equipo eliminado exitosamente',
            'equipo': equipo.nombre
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'mensaje': f'Error al eliminar equipo: {str(e)}'
        }), 500