from flask import Blueprint, request, make_response,jsonify

from celulares import Modelo, Categoria, Equipo
from schemas import ModeloSchema, CategoriaSchema, EquipoSchema

celulares_bp = Blueprint('celulares',__name__)

@celulares_bp.route('/modelo', methods=['GET'])
def modelo():
    modelo = Modelo.query.all()
    return ModeloSchema().dump(modelo, many=True)

@celulares_bp.route('/categoria', methods=['GET'])
def categoria():
    categoria = Categoria.query.all()
    return CategoriaSchema().dump(categoria, many=True)

@celulares_bp.route('/equipos', methods=['GET','POST'])
def equipos():
    if request.method == 'POST':
        data = request.get_json()
        errors = EquipoSchema().validate(data)
        if errors:
            return make_response(jsonify(errors))
        return {}

    equipos = Equipo.query.all()
    return EquipoSchema().dump(equipos, many=True)


@celulares_bp.route('/editar/<id>/modelos', methods=['GET', 'POST'])
def editar_modelo(id):
    modelo = Modelo.query.get_or_404(id)
    if request.method == 'POST':
        data = request.get_json()
        errors = EquipoSchema().validate(data)
        if errors:
            return make_response(jsonify(errors))
        return {}

    equipos = Equipo.query.all()
    return EquipoSchema().dump(equipos, many=True)
