
from abc import ABC
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from aeroalpes.seedwork.dominio.repositorios import Mapeador

class RepositorioProgramas(Repositorio, ABC):
    ...

class MapeadorProgramas(Mapeador, ABC):
    ...