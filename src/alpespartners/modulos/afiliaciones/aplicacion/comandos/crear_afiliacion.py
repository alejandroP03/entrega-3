from alpespartners.seedwork.aplicacion.comandos import Comando
from alpespartners.modulos.afiliaciones.aplicacion.dto import AfiliacionDTO
from .base import CrearAfiliacionBaseHandler
from dataclasses import dataclass, field
from alpespartners.seedwork.aplicacion.comandos import ejecutar_commando as comando

from alpespartners.modulos.afiliaciones.dominio.entidades import Afiliacion
from alpespartners.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from alpespartners.modulos.afiliaciones.aplicacion.mapeadores import MapeadorAfiliacion
from alpespartners.modulos.afiliaciones.dominio.repositorios import RepositorioAfiliaciones

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