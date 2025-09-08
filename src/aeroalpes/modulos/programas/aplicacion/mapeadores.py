
from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.programas.dominio.entidades import Programa
from aeroalpes.modulos.programas.dominio.objetos_valor import TipoPrograma, Marca, EstadoPrograma, VentanaAtribucion, PoliticasCumplimientoAntiFraude
from .dto import ProgramaDTO

class MapeadorProgramaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ProgramaDTO:
        return ProgramaDTO(
            id="",
            nombre=externo.get('nombre'),
            tipo_programa=externo.get('tipo_programa'),
            marca_anunciante_id=externo.get('marca_anunciante_id'),
            marca_anunciante_nombre=externo.get('marca_anunciante_nombre'),
            estado=externo.get('estado'),
            limite_clicks_por_ip=externo.get('limite_clicks_por_ip'),
            limite_velocidad_eventos=externo.get('limite_velocidad_eventos'),
            blacklist_ip=externo.get('blacklist_ip'),
            geo_permitido=externo.get('geo_permitido'),
            duracion_unix_time=externo.get('duracion_unix_time'),
            aplica_desde=externo.get('aplica_desde'),
            fecha_inicio=externo.get('fecha_inicio'),
            fecha_finalizacion=externo.get('fecha_finalizacion'),
            presupuesto=externo.get('presupuesto')
        )

    def dto_a_externo(self, dto: ProgramaDTO) -> dict:
        return dto.__dict__

class MapeadorPrograma(RepMap):
    def obtener_tipo(self) -> type:
        return Programa.__class__

    def entidad_a_dto(self, entidad: Programa) -> ProgramaDTO:
        return ProgramaDTO(
            id=str(entidad.id),
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
            aplica_desde=str(entidad.ventana_atribucion.aplica_desde),
            fecha_inicio=entidad.fecha_inicio,
            fecha_finalizacion=entidad.fecha_finalizacion,
            presupuesto=entidad.presupuesto
        )

    def dto_a_entidad(self, dto: ProgramaDTO) -> Programa:
        programa = Programa()
        programa.nombre = dto.nombre
        programa.tipo_programa = TipoPrograma(estado=dto.tipo_programa)
        programa.marca_anunciante = Marca(id=dto.marca_anunciante_id, nombre=dto.marca_anunciante_nombre)
        programa.estado = EstadoPrograma(estado=dto.estado)
        programa.ventana_atribucion = VentanaAtribucion(
            duracion_unix_time=dto.duracion_unix_time,
            aplica_desde=dto.aplica_desde
        )
        programa.politicas_cumplimiento_antifraude = PoliticasCumplimientoAntiFraude(
            limite_clicks_por_ip=dto.limite_clicks_por_ip,
            limite_velocidad_eventos=dto.limite_velocidad_eventos,
            blacklist_ip=dto.blacklist_ip,
            geo_permitido=dto.geo_permitido
        )
        programa.fecha_inicio = dto.fecha_inicio
        programa.fecha_finalizacion = dto.fecha_finalizacion
        programa.presupuesto = dto.presupuesto
        return programa
