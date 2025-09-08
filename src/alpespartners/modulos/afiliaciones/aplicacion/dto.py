
from dataclasses import dataclass, field
from alpespartners.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class AfiliacionDTO(DTO):
    id_socio: str
    id_programa: str
    estado: str
    fecha_inicio: str
    fecha_fin: str
