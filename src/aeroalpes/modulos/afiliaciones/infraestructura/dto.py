
from aeroalpes.config.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Afiliacion(db.Model):
    __tablename__ = 'afiliaciones'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_socio = db.Column(UUID(as_uuid=True), nullable=False)
    id_programa = db.Column(UUID(as_uuid=True), nullable=False)
    estado = db.Column(db.String, nullable=False)
    fecha_inicio = db.Column(db.String, nullable=False)
    fecha_fin = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
