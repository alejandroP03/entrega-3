
from alpespartners.modulos.programas.dominio.eventos import ProgramaCancelado
from alpespartners.seedwork.aplicacion.handlers import Handler
from alpespartners.modulos.afiliaciones.infraestructura.fabricas import FabricaRepositorio
from alpespartners.modulos.afiliaciones.dominio.repositorios import RepositorioAfiliaciones

class ProgramaCanceladoHandler(Handler):

    @staticmethod
    def handle_programa_cancelado(evento: ProgramaCancelado):
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioAfiliaciones.__class__)

        afiliaciones = repositorio.obtener_por_id_programa(evento.id_programa)

        for afiliacion in afiliaciones:
            # TODO: Check for pending payments
            if True: # No pending payments
                afiliacion.cancelar()
            else: # Pending payments
                afiliacion.suspender()
            repositorio.actualizar(afiliacion)
