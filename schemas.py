from app import ma 

from celulares import *

from marshmallow import validates, ValidationError


class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario
    
    id = ma.auto_field()
    nombre = ma.auto_field()
    password = ma.auto_field()
    is_admin = ma.auto_field()


class MinimalUsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario

    nombre = ma.auto_field()


class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo
    id = ma.auto_field()
    nombre = ma.auto_field()



class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria

    nombre = ma.auto_field()


class EquipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Equipo
    id = ma.auto_field()
    nombre = ma.auto_field()
    costo = ma.auto_field()
    modelo_id = ma.auto_field()
    categoria_id = ma.auto_field()
    activo = ma.auto_field()
    
    @validates('costo')
    def validate_costo(self, value):
        if value < 0: 
            raise ValidationError(
                'el costo no puede ser menor a 0'
                                  )
    

class MinimalEquipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Equipo
    nombre = ma.auto_field()
    costo = ma.auto_field()