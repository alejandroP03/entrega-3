from alpespartners.config.db import db
from alpespartners.seedwork.infraestructura.uow import UnidadTrabajo, Batch
from alpespartners.modulos.programas.dominio.eventos import ProgramaCancelado
from alpespartners.modulos.afiliaciones.aplicacion.handlers import ProgramaCanceladoHandler
from pydispatch import dispatcher

from alpespartners.modulos.programas.infraestructura.fabricas import FabricaRepositorio
from alpespartners.modulos.programas.aplicacion.mapeadores import MapeadorPrograma
from alpespartners.seedwork.aplicacion.comandos import ejecutar_commando
from alpespartners.modulos.programas.aplicacion.comandos.crear_programa import CrearPrograma, CrearProgramaHandler
from alpespartners.modulos.programas.aplicacion.comandos.cancelar_programa import CancelarPrograma, CancelarProgramaHandler

dispatcher.connect(ProgramaCanceladoHandler.handle_programa_cancelado, sender=ProgramaCancelado)

fabrica_repositorio = FabricaRepositorio()
fabrica_mapeador = MapeadorPrograma()

@ejecutar_commando.register(CrearPrograma)
def ejecutar_comando_crear_programa(comando: CrearPrograma):
    handler = CrearProgramaHandler()
    handler.handle(comando)

@ejecutar_commando.register(CancelarPrograma)
def ejecutar_comando_cancelar_programa(comando: CancelarPrograma):
    handler = CancelarProgramaHandler()
    handler.handle(comando)

class UnidadTrabajoSQLAlchemy(UnidadTrabajo):

    def __init__(self):
        self._batches: list[Batch] = list()

    def __enter__(self) -> UnidadTrabajo:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    def _limpiar_batches(self):
        self._batches = list()

    @property
    def savepoints(self) -> list:
        return list[db.session.get_nested_transaction()]

    @property
    def batches(self) -> list[Batch]:
        return self._batches             

    def commit(self):
        for batch in self.batches:
            lock = batch.lock
            batch.operacion(*batch.args, **batch.kwargs)

        db.session.commit()

        super().commit()

    def rollback(self, savepoint=None):
        if savepoint:
            savepoint.rollback()
        else:
            db.session.rollback()
        
        super().rollback()
    
    def savepoint(self):
        db.session.begin_nested()