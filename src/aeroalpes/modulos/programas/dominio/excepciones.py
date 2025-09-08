from aeroalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioProgramasExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fabrica para el tipo solicitado en el modulo de programas'):
        super().__init__(mensaje)

class ProgramaNoEncontradoExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No se encontro el programa'):
        super().__init__(mensaje)