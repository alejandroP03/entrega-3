
from aeroalpes.modulos.programas.dominio.entidades import Programa
from aeroalpes.modulos.programas.dominio.objetos_valor import TipoPrograma, Marca, EstadoPrograma, VentanaAtribucion, PoliticasCumplimientoAntiFraude
from aeroalpes.seedwork.dominio.repositorios import Mapeador
from .dto import Programa as ProgramaDTO

class MapeadorPrograma(Mapeador):

    def obtener_tipo(self) -> type:
        return Programa.__class__

    def entidad_a_dto(self, entidad: Programa) -> ProgramaDTO:
        _id = str(entidad.id)
        return ProgramaDTO(
            id=_id,
            nombre=entidad.nombre,
            tipo_programa=entidad.tipo_programa.estado,
            marca_anunciante_id=entidad.marca_anunciante.id,
            marca_anunciante_nombre=entidad.marca_anunciante.nombre,
            estado=entidad.estado.estado,
            limite_clicks_por_ip=entidad.politicas_cumplimiento_antifraude.limite_clicks_por_ip,
            limite_velocidad_eventos=entidad.politicas_cumplimiento_antifraude.limite_velocidad_eventos,
            blacklist_ip=entidad.politicas_cumplimiento_antifraude.blacklist_ip,
            geo_permitido=entidad.politicas_cumplimiento_antifraude.geo_permitido,
            duracion_unix_time=entidad.ventana_atribucion.duracion_unix_time,
            aplica_desde=entidad.ventana_atribucion.aplica_desde,
            fecha_inicio=entidad.fecha_inicio,
            fecha_finalizacion=entidad.fecha_finalizacion,
            presupuesto=entidad.presupuesto,
            fecha_creacion=entidad.fecha_creacion,
            fecha_actualizacion=entidad.fecha_actualizacion
        )

    def dto_a_entidad(self, dto: ProgramaDTO) -> Programa:
        programa = Programa(
            id=dto.id,
            nombre=dto.nombre,
            tipo_programa=TipoPrograma(estado=dto.tipo_programa),
            marca_anunciante=Marca(id=dto.marca_anunciante_id, nombre=dto.marca_anunciante_nombre),
            estado=EstadoPrograma(estado=dto.estado),
            politicas_cumplimiento_antifraude=PoliticasCumplimientoAntiFraude(
                limite_clicks_por_ip=dto.limite_clicks_por_ip,
                limite_velocidad_eventos=dto.limite_velocidad_eventos,
                blacklist_ip=dto.blacklist_ip,
                geo_permitido=dto.geo_permitido
            ),
            ventana_atribucion=VentanaAtribucion(
                duracion_unix_time=dto.duracion_unix_time,
                aplica_desde=dto.aplica_desde
            ),
            fecha_inicio=dto.fecha_inicio,
            fecha_finalizacion=dto.fecha_finalizacion,
            presupuesto=dto.presupuesto
        )
        programa.fecha_creacion = dto.fecha_creacion
        programa.fecha_actualizacion = dto.fecha_actualizacion
        return programa
