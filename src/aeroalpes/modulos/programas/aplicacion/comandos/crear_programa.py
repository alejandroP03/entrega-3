
from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.programas.aplicacion.dto import ProgramaDTO
from .base import CrearProgramaBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.programas.dominio.entidades import Programa
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.programas.aplicacion.mapeadores import MapeadorPrograma
from aeroalpes.modulos.programas.dominio.repositorios import RepositorioProgramas

@dataclass
class CrearPrograma(Comando):
    programa: ProgramaDTO

class CrearProgramaHandler(CrearProgramaBaseHandler):
    
    def handle(self, comando: CrearPrograma):
        print("Creando programa...")
        programa_dto = comando.programa
        
        mapeador = MapeadorPrograma()
        programa: Programa = mapeador.dto_a_entidad(programa_dto)
        print(f'Programa a crear: {programa}')
        programa.crear_programa(programa)
        print(f'Programa creado: {programa}')

        repositorio = self.repositorio_fabrica.crear_objeto(RepositorioProgramas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, programa)
        UnidadTrabajoPuerto.commit()

        programa = repositorio.obtener_por_id(programa.id)
        comando.programa = mapeador.entidad_a_dto(programa)
        

@comando.register(CrearPrograma)
def ejecutar_comando_crear_programa(comando: CrearPrograma):
    handler = CrearProgramaHandler()
    handler.handle(comando)