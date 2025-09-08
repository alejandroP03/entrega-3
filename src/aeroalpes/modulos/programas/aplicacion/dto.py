
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ProgramaDTO(DTO):
    id: str
    nombre: str
    tipo_programa: str
    marca_anunciante_id: str
    marca_anunciante_nombre: str
    estado: str
    limite_clicks_por_ip: int
    limite_velocidad_eventos: int
    blacklist_ip: bool
    geo_permitido: bool
    duracion_unix_time: int
    aplica_desde: str
    fecha_inicio: str
    fecha_finalizacion: str
    presupuesto: float
