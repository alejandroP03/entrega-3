
from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from aeroalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoPrograma(EventoDominio):
    ...

@dataclass
class ProgramaCreado(EventoPrograma):
    id_programa: uuid.UUID = None
    nombre: str = None
    estado: str = None
    fecha_creacion: datetime = None

@dataclass
class ProgramaCancelado(EventoPrograma):
    id_programa: uuid.UUID = None
    estado: str = None
    fecha_actualizacion: datetime = None

@dataclass
class ProgramaAprobado(EventoPrograma):
    id_programa: uuid.UUID = None
    estado: str = None
    fecha_actualizacion: datetime = None
