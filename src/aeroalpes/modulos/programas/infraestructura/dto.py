
from aeroalpes.config.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Programa(db.Model):
    __tablename__ = 'programas'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String, nullable=False)
    tipo_programa = db.Column(db.String, nullable=False)
    marca_anunciante_id = db.Column(db.String, nullable=False)
    marca_anunciante_nombre = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
    limite_clicks_por_ip = db.Column(db.Integer, nullable=False)
    limite_velocidad_eventos = db.Column(db.Integer, nullable=False)
    blacklist_ip = db.Column(db.ARRAY(db.String), nullable=True)
    geo_permitido = db.Column(db.ARRAY(db.String), nullable=True)
    duracion_unix_time = db.Column(db.Integer, nullable=False)
    aplica_desde = db.Column(db.DateTime, nullable=False)
    fecha_inicio = db.Column(db.String, nullable=False)
    fecha_finalizacion = db.Column(db.String, nullable=False)
    presupuesto = db.Column(db.Float, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
