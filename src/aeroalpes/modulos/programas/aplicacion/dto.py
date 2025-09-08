
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ProgramaDTO(DTO):
    nombre: str
    tipo_programa: str
    marca_anunciante_id: str
    marca_anunciante_nombre: str
    estado: str
    limite_clicks_por_ip: int
    limite_velocidad_eventos: int
    blacklist_ip: list[str]
    geo_permitido: list[str]
    duracion_unix_time: int
    aplica_desde: str
    fecha_inicio: str
    fecha_finalizacion: str
    presupuesto: float
