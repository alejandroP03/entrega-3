
import alpespartners.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for, Response

from alpespartners.modulos.programas.aplicacion.mapeadores import MapeadorProgramaDTOJson
from alpespartners.modulos.programas.aplicacion.comandos.crear_programa import CrearPrograma
from alpespartners.modulos.programas.aplicacion.comandos.cancelar_programa import CancelarPrograma
from alpespartners.modulos.programas.aplicacion.queries.obtener_programas import ObtenerProgramas
from alpespartners.modulos.afiliaciones.aplicacion.mapeadores import MapeadorAfiliacionDTOJson
from alpespartners.modulos.afiliaciones.aplicacion.queries.obtener_afiliaciones_programa import ObtenerAfiliacionesPrograma
from alpespartners.seedwork.aplicacion.comandos import ejecutar_commando
from alpespartners.seedwork.aplicacion.queries import ejecutar_query
from alpespartners.seedwork.dominio.excepciones import ExcepcionDominio

from alpespartners.modulos.programas.aplicacion.queries.obtener_programas import ObtenerProgramas

bp = api.crear_blueprint('programas', '/programas')

@bp.route('/', methods=('GET',))
def obtener_programas():
    try:
        query_resultado = ejecutar_query(ObtenerProgramas())
        map_programa = MapeadorProgramaDTOJson()
        return Response(json.dumps([map_programa.dto_a_externo(resultado) for resultado in query_resultado.resultado]), status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/', methods=('POST',))
def crear_programa():
    try:
        programa_dict = request.json
        map_programa = MapeadorProgramaDTOJson()
        programa_dto = map_programa.externo_a_dto(programa_dict)
        
        comando = CrearPrograma(programa=programa_dto)

        ejecutar_commando(comando)
        return Response(json.dumps(map_programa.dto_a_externo(comando.programa)), status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/<id>/cancelar', methods=('POST',))
def cancelar_programa(id):
    try:
        comando = CancelarPrograma(id_programa=id)
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/<id>/afiliaciones', methods=('GET',))
def obtener_afiliaciones_programa(id):
    try:
        query_resultado = ejecutar_query(ObtenerAfiliacionesPrograma(id_programa=id))
        map_afiliacion = MapeadorAfiliacionDTOJson()
        return [map_afiliacion.dto_a_externo(resultado) for resultado in query_resultado.resultado]
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')