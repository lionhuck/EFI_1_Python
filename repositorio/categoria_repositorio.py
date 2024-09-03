from app import db
from celulares import Categoria

class CategoriaRepositorio:
    """
    Va a ser la clase encargada de manejar el modelo en la DB
    """
    def get_all(self):
        return Categoria.query.all()
    
    def create(self, nombre):
        nueva_categoria = Categoria(nombre=nombre)
        db.session.add(nueva_categoria)
        db.session.commit()
        return nueva_categoria
