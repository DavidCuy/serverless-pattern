import json
import decimal
import datetime
from json.encoder import JSONEncoder
from typing import Dict, Tuple

class CustomJSONDecoder(json.JSONEncoder):
    """ Clase que ayuda con el manejo de JSON de un blob Storage de Azure
    """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        if isinstance(o, bytes):
            return o.decode()
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return super(CustomJSONDecoder, self).default(o)

def build_response(status: int, body: dict or str, jsonEncoder: JSONEncoder = CustomJSONDecoder, circular: bool = True, is_body_str: bool = False, encoder_extras: dict = {}) -> Dict:
    """ Devuelve el formato que acepta azure para una respuesta de HTTP

    Args:
        status (int): Codido http
        body (dict): Contenido del json de respuesta
        jsonEncoder (JSONEncoder, optional): Codificacion el JSON de salida. Defaults to CustomJSONDecoder.
        circular (bool, optional): Inidica si la codificacion la hara por cada parametro del JSON. Defaults to True.

    Returns:
        func.HttpResponse: Respuesta HTTP aceptada por Azure
    """
    return {
        "statusCode": status,
        "body": body if type(body) is str else json.dumps(body, cls=jsonEncoder, check_circular=circular, **encoder_extras),
        "headers":  {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
            }
    }


def serialize_json(data: dict, jsonEncoder: JSONEncoder = CustomJSONDecoder, circular: bool = True) -> str:
    """ Devuelve una cadena en formato JSON de un objeto

    Args:
        data (dict): Contenido del json de respuesta
        jsonEncoder (JSONEncoder, optional): Codificacion el JSON de salida. Defaults to CustomJSONDecoder.
        circular (bool, optional): Inidica si la codificacion la hara por cada parametro del JSON. Defaults to True.

    Returns:
        str: Cadena con formato JSON del contenido
    """
    return json.dumps(data, cls=jsonEncoder, check_circular=circular)

def get_paginate_params(req: dict) -> Tuple[bool, int, int]:
    """ Devuelve los parametros de paginacion de una peticion http

    Args:
        req (func.HttpRequest): Peticion http

    Returns:
        Tuple[bool, int, int]: Parametros de paginacion (Paginado, num de pagina, elementos por pagina)
    """

    if req is None:
        return (1, 100)

    if 'page' in req:
        page = int(req['page'])
    else:
        page = 1

    if 'per_page' in req:
        per_page = int(req['per_page'])
    else:
        per_page = 100
    
    return (page, per_page)

def get_filter_params(req: dict) -> dict:
    """ Obtiene filtros de query

    Args:
        req (dict): Peticion http

    Returns:
        dict: Filtros formados como par valor
    """
    if req is None:
        return {}
    
    ret_dict = {}
    for key in req.keys():
        if key == 'page' or key == 'per_page' or key == 'relationships':
            pass
        else:
            ret_dict.update({key: req[key]})
    
    return ret_dict

def get_relationship_params(req: dict) -> dict:
    """ Obtiene filtros de query

    Args:
        req (dict): Peticion http

    Returns:
        dict: Filtros formados como par valor
    """
    if req is None:
        return {}
    
    ret_dict = {}
    if 'relationships' in req.keys():
        ret_dict.update(dict(relationships=req['relationships']))
    
    return ret_dict
 
def get_search_params(req: dict) -> dict:
    """ Obtiene filtros de query

    Args:
        req (dict): Peticion http

    Returns:
        dict: Filtros formados como par valor
    """
    if req is None:
        return {}
    
    ret_dict = {}
    for k in req.keys():
            
        if str(k).startswith('search-'):
            key = str(k).split('-')[1]
            ret_dict[key] = str(req[k]).replace('*', '%')
    
    return ret_dict
 
def get_search_method_param(req: dict) -> str:
    """ Obtiene el metodo de filtrado de query

    Args:
        req (dict): Peticion http

    Returns:
        str: Metodo de filtraddo
    """
    if req is None:
        return 'AND'
    if 'searchmethod' not in req:
        return 'AND'
    
    method = str(req['searchmethod']).upper()
    return 'AND' if method not in ['AND', 'OR'] else method
        