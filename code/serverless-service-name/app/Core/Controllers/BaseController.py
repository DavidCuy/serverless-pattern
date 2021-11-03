import json
from typing import cast
import logging

from app.Exceptions.APIException import APIException

from ..Services.BaseService import BaseService

from app.Data.Interfaces.PaginationResult import PaginationResult
from database.DBConnection import AlchemyEncoder, get_session
from utils.http_utils import build_response, get_paginate_params
from app.Data.Enum.http_status_code import HTTPStatusCode

def index(service, event: dict):
    session = get_session()
    (page, per_page) = get_paginate_params(event['queryStringParameters'])
    
    try:
        elements = cast(BaseService, service).get_all(session, True, page, per_page)
        total_elements = cast(BaseService, service).count_elements(session)
        body = PaginationResult(elements, page, per_page, total_elements).to_dict()
        status_code = HTTPStatusCode.OK.value
    except APIException as e:
        logging.exception("APIException occurred")
        body = e.to_dict()
        status_code = e.status_code
    except Exception as e:
        logging.exception("Cannot make the request")
        body = dict(message="Cannot make the request")
        status_code = HTTPStatusCode.UNPROCESABLE_ENTITY.value
    finally:
        session.close()
    return build_response(status_code, body, jsonEncoder=AlchemyEncoder)

def find(service, event: dict):
    session = get_session()
    path_params = event['pathParameters']
    id = int(path_params['id'])
    try:
        body = cast(BaseService, service).get_one(session, id)
        status_code = HTTPStatusCode.OK.value
    except APIException as e:
        logging.exception("APIException occurred")
        body = e.to_dict()
        status_code = e.status_code
    except Exception as e:
        logging.exception("Cannot make the request")
        body = dict(message="Cannot make the request")
        status_code = HTTPStatusCode.UNPROCESABLE_ENTITY.value
    finally:
        session.close()
    return build_response(status_code, body, jsonEncoder=AlchemyEncoder)

def store(service, event: dict):
    session = get_session()
    
    input_params = json.loads(event.get('body'))

    try:
        body = cast(BaseService, service).insert_register(session, input_params)
        response = json.dumps(body, cls=AlchemyEncoder)
        status_code = HTTPStatusCode.OK.value
    except APIException as e:
        logging.exception("APIException occurred")
        response = json.dumps(e.to_dict())
        status_code = e.status_code
    except Exception:
        logging.exception("No se pudo realizar la consulta")
        body = dict(message="No se pudo realizar la consulta")
        response = json.dumps(body)
        status_code=HTTPStatusCode.UNPROCESABLE_ENTITY.value
    finally:
        session.close()
    
    return build_response(status_code, response, is_body_str=True)

def update(service, event: dict):
    session = get_session()
    path_params = event['pathParameters']
    id = int(path_params['id'])

    input_params = json.loads(event.get('body'))
    try:
        body = cast(BaseService, service).update_register(session, id, input_params)
        response = json.dumps(body, cls=AlchemyEncoder)
        status_code = HTTPStatusCode.OK.value
    except APIException as e:
        logging.exception("APIException occurred")
        response = json.dumps(e.to_dict())
        status_code = e.status_code
    except Exception as e:
        logging.exception("Cannot make the request")
        body = dict(message="Cannot make the request")
        response = json.dumps(body)
        status_code = HTTPStatusCode.UNPROCESABLE_ENTITY.value
    finally:
        session.close()
    return build_response(status_code, response, is_body_str=True)

def delete(service, event: dict):
    session = get_session()
    path_params = event['pathParameters']
    id = int(path_params['id'])

    try:
        body = cast(BaseService, service).delete_register(session, id)
        status_code = HTTPStatusCode.OK.value
    except APIException as e:
        logging.exception("APIException occurred")
        body = e.to_dict()
        status_code = e.status_code
    except Exception as e:
        logging.exception("Cannot make the request")
        body = dict(message="Cannot make the request")
        status_code = HTTPStatusCode.UNPROCESABLE_ENTITY.value
    finally:
        session.close()
    return build_response(status_code, body, jsonEncoder=AlchemyEncoder)
