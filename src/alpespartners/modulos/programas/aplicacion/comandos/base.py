
from alpespartners.seedwork.aplicacion.comandos import ComandoHandler
from alpespartners.modulos.programas.infraestructura.fabricas import FabricaRepositorio
from alpespartners.modulos.programas.dominio.fabricas import FabricaProgramas


class CrearProgramaBaseHandler(ComandoHandler):
    def __init__(self):
        self._repositorio_fabrica: FabricaRepositorio = FabricaRepositorio()
        self._mapeador_fabrica: FabricaProgramas = FabricaProgramas()

    @property
    def repositorio_fabrica(self):
        return self._repositorio_fabrica

    @property
    def mapeador_fabrica(self):
        return self._mapeador_fabrica

class CancelarProgramaBaseHandler(ComandoHandler):
    def __init__(self):
        self._repositorio_fabrica = FabricaRepositorio()
        self._mapeador_fabrica = FabricaProgramas()

    @property
    def repositorio_fabrica(self):
        return self._repositorio_fabrica

    @property
    def mapeador_fabrica(self):
        return self._mapeador_fabrica      