
from aeroalpes.seedwork.aplicacion.comandos import ComandoHandler

class ProgramaComandoBaseHandler(ComandoHandler):
    def __init__(self):
        self._repositorio_fabrica = None
        self._mapeador_fabrica = None

    @property
    def repositorio_fabrica(self):
        return self._repositorio_fabrica

    @property
    def mapeador_fabrica(self):
        return self._mapeador_fabrica
