import aeroalpes.seedwork.presentacion.api as api
import json
from flask import Response, request

from aeroalpes.modulos.afiliaciones.aplicacion.mapeadores import MapeadorAfiliacionDTOJson
from aeroalpes.modulos.afiliaciones.aplicacion.comandos.crear_afiliacion import CrearAfiliacion
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('afiliaciones', '/afiliaciones')

@bp.route('/', methods=('POST',))
def crear_afiliacion():
    try:
        afiliacion_dict = request.json
        map_afiliacion = MapeadorAfiliacionDTOJson()
        afiliacion_dto = map_afiliacion.externo_a_dto(afiliacion_dict)
        
        comando = CrearAfiliacion(afiliacion=afiliacion_dto)
        ejecutar_commando(comando)
        dto_final = comando.afiliacion
        return Response(json.dumps(map_afiliacion.dto_a_externo(dto_final)), status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')