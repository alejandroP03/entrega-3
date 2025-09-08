from aeroalpes.modulos.afiliaciones.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.afiliaciones.infraestructura.mapeadores import MapeadorAfiliacion
from aeroalpes.seedwork.aplicacion.queries import QueryHandler

class AfiliacionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._repositorio_fabrica = FabricaRepositorio()
        self._mapeador_fabrica = MapeadorAfiliacion()

    @property
    def repositorio_fabrica(self):
        return self._repositorio_fabrica

    @property
    def mapeador_fabrica(self):
        return self._mapeador_fabrica
