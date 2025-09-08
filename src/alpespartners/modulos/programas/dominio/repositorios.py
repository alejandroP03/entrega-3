
from abc import ABC
from alpespartners.seedwork.dominio.repositorios import Repositorio
from alpespartners.seedwork.dominio.repositorios import Mapeador

class RepositorioProgramas(Repositorio, ABC):
    ...

class MapeadorProgramas(Mapeador, ABC):
    ...