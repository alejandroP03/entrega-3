
from alpespartners.config.db import db
from alpespartners.modulos.afiliaciones.dominio.repositorios import RepositorioAfiliaciones
from alpespartners.modulos.afiliaciones.dominio.entidades import Afiliacion
from .dto import Afiliacion as AfiliacionDTO
from .mapeadores import MapeadorAfiliacion
import uuid

class RepositorioAfiliacionesPostgreSQL(RepositorioAfiliaciones):

    def __init__(self):
        self._mapeador = MapeadorAfiliacion()

    @property
    def mapeador(self):
        return self._mapeador

    def obtener_por_id(self, id: uuid.UUID) -> Afiliacion:
        afiliacion_dto = db.session.query(AfiliacionDTO).filter_by(id=str(id)).one()
        return self.mapeador.dto_a_entidad(afiliacion_dto)

    def obtener_todos(self) -> list[Afiliacion]:
        afiliaciones_dto = db.session.query(AfiliacionDTO).all()
        return [self.mapeador.dto_a_entidad(dto) for dto in afiliaciones_dto]

    def obtener_por_id_programa(self, id_programa: uuid.UUID) -> list[Afiliacion]:
        afiliaciones_dto = db.session.query(AfiliacionDTO).filter_by(id_programa=str(id_programa)).all()
        return [self.mapeador.dto_a_entidad(dto) for dto in afiliaciones_dto]

    def agregar(self, afiliacion: Afiliacion):
        afiliacion_dto = self.mapeador.entidad_a_dto(afiliacion)
        db.session.add(afiliacion_dto)

    def actualizar(self, afiliacion: Afiliacion):
        afiliacion_dto = self.mapeador.entidad_a_dto(afiliacion)
        db.session.query(AfiliacionDTO).filter_by(id=str(afiliacion.id)).update(afiliacion_dto)

    def eliminar(self, id: uuid.UUID):
        db.session.query(AfiliacionDTO).filter_by(id=str(id)).delete()
