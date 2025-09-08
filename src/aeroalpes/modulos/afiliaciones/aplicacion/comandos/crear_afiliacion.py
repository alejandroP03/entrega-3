from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.afiliaciones.aplicacion.dto import AfiliacionDTO
from .base import CrearAfiliacionBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.afiliaciones.dominio.entidades import Afiliacion
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.afiliaciones.aplicacion.mapeadores import MapeadorAfiliacion
from aeroalpes.modulos.afiliaciones.dominio.repositorios import RepositorioAfiliaciones

@dataclass
class CrearAfiliacion(Comando):
    afiliacion: AfiliacionDTO

class CrearAfiliacionHandler(CrearAfiliacionBaseHandler):
    
    def handle(self, comando: CrearAfiliacion):
        afiliacion_dto = comando.afiliacion
        
        mapeador = MapeadorAfiliacion()
        afiliacion = mapeador.dto_a_entidad(afiliacion_dto)

        repositorio = self.repositorio_fabrica.crear_objeto(RepositorioAfiliaciones.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, afiliacion)
        UnidadTrabajoPuerto.commit()


@comando.register(CrearAfiliacion)
def ejecutar_comando_crear_afiliacion(comando: CrearAfiliacion):
    handler = CrearAfiliacionHandler()
    handler.handle(comando)