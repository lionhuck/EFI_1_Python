from app import db
from celulares import Pais


class PaisRepository:
    """
    va a ser la clase encargada de manejar el modelo de la BD
    """

    def get_all(self):
        return Pais.query.all()
    
    def create(self,nombre):
        nuevo_pais = Pais(nombre = nombre)
        db.session.add(nuevo_pais)
        db.session.commit()
        return nuevo_pais
