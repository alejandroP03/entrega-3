
from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import aeroalpes.modulos.programas.dominio.objetos_valor as ov
from aeroalpes.modulos.programas.dominio.eventos import ProgramaCreado, ProgramaCancelado, ProgramaAprobado
from aeroalpes.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Programa(AgregacionRaiz):
    id_programa: uuid.UUID = field(hash=True, default=None)
    nombre: str = field(default=None)
    tipo_programa: ov.TipoPrograma = field(default=None)
    marca_anunciante: ov.Marca = field(default=None)
    estado: ov.EstadoPrograma = field(default=None)
    ventana_atribucion: ov.VentanaAtribucion = field(default=None)
    fecha_inicio: str = field(default=None)
    fecha_finalizacion: str = field(default=None)
    presupuesto: float = field(default=None)

    def crear_programa(self, programa: Programa):
        self.id_programa = programa.id_programa
        self.nombre = programa.nombre
        self.tipo_programa = programa.tipo_programa
        self.marca_anunciante = programa.marca_anunciante
        self.estado = programa.estado
        self.ventana_atribucion = programa.ventana_atribucion
        self.fecha_inicio = programa.fecha_inicio
        self.fecha_finalizacion = programa.fecha_finalizacion
        self.presupuesto = programa.presupuesto

        self.agregar_evento(ProgramaCreado(id_programa=self.id, nombre=self.nombre, estado=self.estado.estado, fecha_creacion=self.fecha_creacion))

    def cancelar_programa(self):
        self.estado = ov.EstadoPrograma(estado='CANCELADO')
        self.agregar_evento(ProgramaCancelado(id_programa=self.id, estado=self.estado.estado, fecha_actualizacion=self.fecha_actualizacion))

    def aprobar_programa(self):
        self.estado = ov.EstadoPrograma(estado='APROBADO')
        self.agregar_evento(ProgramaAprobado(id_programa=self.id, estado=self.estado.estado, fecha_actualizacion=self.fecha_actualizacion))
