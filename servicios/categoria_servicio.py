from repositorio.categoria_repositorio import CategoriaRepositorio

class CategoriaServicio:
    def __init__(
        self, categoria_repository: CategoriaRepositorio
            ):
        self._categoria_repository = categoria_repository
        
    def get_all(self):
        return self._categoria_repository.get_all()
    
    def create(self, nombre):
        categoria = self._categoria_repository.create(nombre)
        return categoria