
from dataclasses import dataclass, field
from alpespartners.seedwork.dominio.fabricas import Fabrica
from alpespartners.seedwork.dominio.repositorios import Repositorio
from alpespartners.modulos.afiliaciones.dominio.repositorios import RepositorioAfiliaciones
from .repositorios import RepositorioAfiliacionesPostgreSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAfiliaciones.__class__:
            return RepositorioAfiliacionesPostgreSQL()
        else:
            raise ExcepcionFabrica(f'No existe fabrica para el objeto {obj}')
