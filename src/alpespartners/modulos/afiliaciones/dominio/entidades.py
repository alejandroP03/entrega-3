
from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import alpespartners.modulos.afiliaciones.dominio.objetos_valor as ov
from alpespartners.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Afiliacion(AgregacionRaiz):
    id_afiliacion: uuid.UUID = field(hash=True, default=None)
    id_socio: uuid.UUID = field(default=None)
    id_programa: uuid.UUID = field(default=None)
    estado: ov.EstadoAfiliacion = field(default=None)
    fecha_inicio: str = field(default=None)
    fecha_fin: str = field(default=None)

    def cancelar(self):
        self.estado = ov.EstadoAfiliacion(estado='CANCELADO')

    def suspender(self):
        self.estado = ov.EstadoAfiliacion(estado='SUSPENDIDO')
