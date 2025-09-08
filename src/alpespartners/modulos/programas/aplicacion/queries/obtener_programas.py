
from alpespartners.seedwork.aplicacion.queries import Query, QueryResultado
from alpespartners.seedwork.aplicacion.queries import ejecutar_query as query
from alpespartners.modulos.programas.infraestructura.fabricas import FabricaRepositorio
from alpespartners.modulos.programas.infraestructura.repositorios import RepositorioProgramas
from alpespartners.modulos.programas.aplicacion.mapeadores import MapeadorPrograma
from .base import ProgramaQueryBaseHandler
from dataclasses import dataclass

@dataclass
class ObtenerProgramas(Query):
    ...

class ObtenerProgramasHandler(ProgramaQueryBaseHandler):

    def handle(self, query: ObtenerProgramas) -> QueryResultado:
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioProgramas.__class__)
        programas = repositorio.obtener_todos()
        mapeador = MapeadorPrograma()
        return QueryResultado(resultado=[mapeador.entidad_a_dto(programa) for programa in programas])

@query.register(ObtenerProgramas)
def ejecutar_query_obtener_programas(query: ObtenerProgramas):
    handler = ObtenerProgramasHandler()
    return handler.handle(query)