from repositories.paises_repository import PaisRepository

class PaisService:

    def __init__(
            self,pais_repository: PaisRepository
    ):
        self._pais_repository = pais_repository

    def get_all(self):
        return self._pais_repository.get_all()
    

    def create(self,nombre):
        pais = self._pais_repository.create(nombre)
        return pais