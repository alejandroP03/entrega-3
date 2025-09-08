
from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from .base import AfiliacionQueryBaseHandler
from dataclasses import dataclass
from aeroalpes.modulos.afiliaciones.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.afiliaciones.aplicacion.mapeadores import MapeadorAfiliacion

@dataclass
class ObtenerAfiliacionesPrograma(Query):
    id_programa: str

class ObtenerAfiliacionesProgramaHandler(AfiliacionQueryBaseHandler):

    def handle(self, query: ObtenerAfiliacionesPrograma) -> QueryResultado:
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(fabrica_repositorio.RepositorioAfiliaciones.__class__)
        afiliaciones = repositorio.obtener_por_id_programa(query.id_programa)
        mapeador = MapeadorAfiliacion()
        return QueryResultado(resultado=[mapeador.entidad_a_dto(afiliacion) for afiliacion in afiliaciones])
