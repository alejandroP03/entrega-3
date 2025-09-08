from alpespartners.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from alpespartners.modulos.afiliaciones.dominio.repositorios import RepositorioAfiliaciones
from alpespartners.modulos.afiliaciones.infraestructura.fabricas import FabricaRepositorio

class CrearAfiliacionBaseHandler:
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def repositorio_fabrica(self):
        return self._fabrica_repositorio