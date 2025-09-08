
from alpespartners.seedwork.aplicacion.dto import Mapeador as AppMap
from alpespartners.seedwork.dominio.repositorios import Mapeador as RepMap
from alpespartners.modulos.afiliaciones.dominio.entidades import Afiliacion
from alpespartners.modulos.afiliaciones.dominio.objetos_valor import EstadoAfiliacion
from .dto import AfiliacionDTO

class MapeadorAfiliacionDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> AfiliacionDTO:
        return AfiliacionDTO(
            id_socio=externo.get('id_socio'),
            id_programa=externo.get('id_programa'),
            estado=externo.get('estado'),
            fecha_inicio=externo.get('fecha_inicio'),
            fecha_fin=externo.get('fecha_fin')
        )

    def dto_a_externo(self, dto: AfiliacionDTO) -> dict:
        return dto.__dict__

class MapeadorAfiliacion(RepMap):
    def obtener_tipo(self) -> type:
        return Afiliacion.__class__

    def entidad_a_dto(self, entidad: Afiliacion) -> AfiliacionDTO:
        return AfiliacionDTO(
            id_socio=str(entidad.id_socio),
            id_programa=str(entidad.id_programa),
            estado=entidad.estado.estado,
            fecha_inicio=entidad.fecha_inicio,
            fecha_fin=entidad.fecha_fin
        )

    def dto_a_entidad(self, dto: AfiliacionDTO) -> Afiliacion:
        return Afiliacion(
            id_socio=dto.id_socio,
            id_programa=dto.id_programa,
            estado=EstadoAfiliacion(estado=dto.estado),
            fecha_inicio=dto.fecha_inicio,
            fecha_fin=dto.fecha_fin
        )
