
from alpespartners.seedwork.dominio.excepciones import ExcepcionFabrica

class NoExisteImplementacionParaTipoFabricaExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una implementacion para el repositorio con la fabrica dada'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
