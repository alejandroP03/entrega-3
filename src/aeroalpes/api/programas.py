
import aeroalpes.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for, Response

from aeroalpes.modulos.programas.aplicacion.mapeadores import MapeadorProgramaDTOJson
from aeroalpes.modulos.programas.aplicacion.comandos.crear_programa import CrearPrograma
from aeroalpes.modulos.programas.aplicacion.comandos.cancelar_programa import CancelarPrograma
from aeroalpes.modulos.afiliaciones.aplicacion.mapeadores import MapeadorAfiliacionDTOJson
from aeroalpes.modulos.afiliaciones.aplicacion.queries.obtener_afiliaciones_programa import ObtenerAfiliacionesPrograma
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('programas', '/programas')

@bp.route('/hello', methods=('GET',))
def hello():
    return 'Hello, World!'

@bp.route('/', methods=('POST',))
def crear_programa():
    try:
        programa_dict = request.json
        map_programa = MapeadorProgramaDTOJson()
        programa_dto = map_programa.externo_a_dto(programa_dict)
        comando = CrearPrograma(programa=programa_dto)
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
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
