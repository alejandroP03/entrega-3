from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.afiliaciones.dominio.repositorios import RepositorioAfiliaciones
from aeroalpes.modulos.afiliaciones.infraestructura.fabricas import FabricaRepositorio

class CrearAfiliacionBaseHandler:
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def repositorio_fabrica(self):
        return self._fabrica_repositorio