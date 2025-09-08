
from dataclasses import dataclass, field
from alpespartners.seedwork.dominio.fabricas import Fabrica
from alpespartners.seedwork.dominio.repositorios import Repositorio
from alpespartners.modulos.programas.dominio.repositorios import RepositorioProgramas
from .repositorios import RepositorioProgramasPostgreSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioProgramas.__class__:
            return RepositorioProgramasPostgreSQL()
        else:
            raise ExcepcionFabrica(f'No existe fabrica para el objeto {obj}')
