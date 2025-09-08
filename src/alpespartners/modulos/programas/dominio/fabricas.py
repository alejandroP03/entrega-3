from .entidades import Programa
from .excepciones import TipoObjetoNoExisteEnDominioProgramasExcepcion
from alpespartners.seedwork.dominio.repositorios import Mapeador, Repositorio
from alpespartners.seedwork.dominio.fabricas import Fabrica
from alpespartners.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaProgramas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Programa.__class__:
            fabrica_programa = FabricaProgramas()
            return fabrica_programa.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioProgramasExcepcion()