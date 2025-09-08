
from aeroalpes.seedwork.aplicacion.comandos import Comando
from .base import CancelarProgramaBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.programas.dominio.entidades import Programa
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.programas.dominio.repositorios import RepositorioProgramas

@dataclass
class CancelarPrograma(Comando):
    id_programa: str

class CancelarProgramaHandler(CancelarProgramaBaseHandler):
    
    def handle(self, comando: CancelarPrograma):
        repositorio = self.repositorio_fabrica.crear_objeto(RepositorioProgramas.__class__)
        programa = repositorio.obtener_por_id(comando.id_programa)
        programa.cancelar_programa()

        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, programa)
        UnidadTrabajoPuerto.commit()

@comando.register(CancelarPrograma)
def ejecutar_comando_cancelar_programa(comando: CancelarPrograma):
    handler = CancelarProgramaHandler()
    handler.handle(comando)