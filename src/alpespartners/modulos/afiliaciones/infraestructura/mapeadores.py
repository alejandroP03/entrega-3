
from alpespartners.modulos.afiliaciones.dominio.entidades import Afiliacion
from alpespartners.modulos.afiliaciones.dominio.objetos_valor import EstadoAfiliacion
from alpespartners.seedwork.dominio.repositorios import Mapeador
from .dto import Afiliacion as AfiliacionDTO

class MapeadorAfiliacion(Mapeador):

    def obtener_tipo(self) -> type:
        return Afiliacion.__class__

    def entidad_a_dto(self, entidad: Afiliacion) -> AfiliacionDTO:
        _id = str(entidad.id)
        return AfiliacionDTO(
            id=_id,
            id_socio=entidad.id_socio,
            id_programa=entidad.id_programa,
            estado=entidad.estado.estado,
            fecha_inicio=entidad.fecha_inicio,
            fecha_fin=entidad.fecha_fin,
            fecha_creacion=entidad.fecha_creacion,
            fecha_actualizacion=entidad.fecha_actualizacion
        )

    def dto_a_entidad(self, dto: AfiliacionDTO) -> Afiliacion:
        afiliacion = Afiliacion(
            id=dto.id,
            id_socio=dto.id_socio,
            id_programa=dto.id_programa,
            estado=EstadoAfiliacion(estado=dto.estado),
            fecha_inicio=dto.fecha_inicio,
            fecha_fin=dto.fecha_fin
        )
        afiliacion.fecha_creacion = dto.fecha_creacion
        afiliacion.fecha_actualizacion = dto.fecha_actualizacion
        return afiliacion
