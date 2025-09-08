
from aeroalpes.config.db import db
from aeroalpes.modulos.programas.dominio.repositorios import RepositorioProgramas
from aeroalpes.modulos.programas.dominio.entidades import Programa
from .dto import Programa as ProgramaDTO
from .mapeadores import MapeadorPrograma
import uuid

class RepositorioProgramasPostgreSQL(RepositorioProgramas):

    def __init__(self):
        self._mapeador = MapeadorPrograma()

    @property
    def mapeador(self):
        return self._mapeador

    def obtener_por_id(self, id: uuid.UUID) -> Programa:
        programa_dto = db.session.query(ProgramaDTO).filter_by(id=str(id)).one()
        return self.mapeador.dto_a_entidad(programa_dto)

    def obtener_todos(self) -> list[Programa]:
        programas_dto = db.session.query(ProgramaDTO).all()
        return [self.mapeador.dto_a_entidad(dto) for dto in programas_dto]

    def agregar(self, programa: Programa):
        programa_dto = self.mapeador.entidad_a_dto(programa)
        db.session.add(programa_dto)

    def actualizar(self, programa: Programa):
        programa_dto = self.mapeador.entidad_a_dto(programa)
        db.session.query(ProgramaDTO).filter_by(id=str(programa.id)).update(programa_dto)

    def eliminar(self, id: uuid.UUID):
        db.session.query(ProgramaDTO).filter_by(id=str(id)).delete()
