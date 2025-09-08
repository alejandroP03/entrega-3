
from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from .base import AfiliacionQueryBaseHandler
from dataclasses import dataclass
from aeroalpes.modulos.afiliaciones.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.afiliaciones.infraestructura.repositorios import RepositorioAfiliaciones
from aeroalpes.modulos.afiliaciones.aplicacion.mapeadores import MapeadorAfiliacion

@dataclass
class ObtenerAfiliacionesPrograma(Query):
    id_programa: str

class ObtenerAfiliacionesProgramaHandler(AfiliacionQueryBaseHandler):

    def handle(self, query: ObtenerAfiliacionesPrograma) -> QueryResultado:
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioAfiliaciones.__class__)
        afiliaciones = repositorio.obtener_por_id_programa(query.id_programa)
        mapeador = MapeadorAfiliacion()
        return QueryResultado(resultado=[mapeador.entidad_a_dto(afiliacion) for afiliacion in afiliaciones])

@query.register(ObtenerAfiliacionesPrograma)
def ejecutar_query_obtener_afiliaciones_programa(query: ObtenerAfiliacionesPrograma) -> QueryResultado:
    handler = ObtenerAfiliacionesProgramaHandler()
    return handler.handle(query)