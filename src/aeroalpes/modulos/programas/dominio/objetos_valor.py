
from __future__ import annotations
from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Marca:
    id: str
    nombre: str

@dataclass(frozen=True)
class EstadoPrograma:
    estado: str

@dataclass(frozen=True)
class PoliticasCumplimientoAntiFraude:
    limite_clicks_por_ip: int
    limite_velocidad_eventos: int
    blacklist_ip: bool
    geo_permitido: bool

@dataclass(frozen=True)
class VentanaAtribucion:
    duracion_unix_time: int
    aplica_desde: str

@dataclass(frozen=True)
class TipoPrograma:
    estado: str

