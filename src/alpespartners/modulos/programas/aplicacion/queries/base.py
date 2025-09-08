from alpespartners.seedwork.aplicacion.queries import QueryHandler
from alpespartners.modulos.programas.infraestructura.fabricas import FabricaRepositorio

class ProgramaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio