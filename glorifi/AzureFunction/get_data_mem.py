import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
import logging
import json
import traceback
import distutils
from sqlalchemy import false
import shared_code.responses as responses
import azure.functions as func
from shared_code.database_calls import call_pg_function
from marshmallow import Schema, fields
from shared_code.utilities import validate_request

class MemberAddrSchema(Schema):
    member_id = fields.Integer(required=True)
    addr_type = fields.Integer()
    limit1 = fields.Boolean()


def main(req: func.HttpRequest) -> func.HttpResponse:
    """ 
    API for getting address of a member based on 
    member_id and addr_type

    Parameters : 
        member_id as route parameter
        addr_type as query string ( optional )

    This function expects a valid member_id to be passed
    in order to get a response with all address details
    addr_type can be given in the query string to only show
    addresses of that type
    """
    logging.info('Python HTTP trigger function processed a request.')
    logging.info("req.url: %s", req.url)
    logging.info("req.route_params %s",req.route_params)
    logging.info("req.params %s",req.params)

    code = responses.CODE_INTERNAL_ERROR
    message = {"message":"Internal Server Error"}
    req_data = {}
    query_param= []

    try :
        member_id = req.route_params.get('member_id')
        logging.info('member_id: %s', member_id)

        addr_type = req.params.get('addr_type')
        logging.info('addr_type: %s', addr_type)

        limit1 = req.params.get('limit1')
        logging.info('limit1: %s', limit1)
        
        req_data['member_id'] = member_id
        query_param.append(member_id)

        if limit1 is None:
            limit1 = True
        elif limit1 == 'True' or limit1 == 'true' or limit1 == '1':
            limit1 = False
        else:
            limit1 = True

        if addr_type is not None:
            if addr_type == '99':
                limit1 = False
            req_data['addr_type'] = addr_type
            query_param.append(addr_type)

        # Request Parameter Validation
        ma_schema = MemberAddrSchema()
        req_invalid, validation_errors = validate_request(req_data, ma_schema)
        if req_invalid:
            logging.info("Request is not valid")
            code = responses.BAD_REQUEST
            message = validation_errors

        else:
            logging.info("Request is valid")

            # Check if the member_id exists
            status_1, member_exist = call_pg_function('datahub.member_exists_check', [member_id], False)
            if status_1 : 
                logging.info("SQL statement successfully executed")
                member_exist = member_exist.get('member_exists_check')
                logging.info("member_exist: {0}".format(member_exist)) 

                if member_exist: 
                    status_2, output = call_pg_function('datahub.get_member_address', query_param, limit1)
                    if  status_2:
                        # The SQL function executed successfully
                        logging.info("SQL statement successfully executed")  

                        if output:
                            code = responses.SUCCESSFUL_RESPONSE
                            message = {"Address" : output}
                            
                        else:
                            code = responses.ADDR_TYPE_DOESNT_EXIST_RESPONSE
                            message = {"message" :"This HTTP triggered function executed successfully; however, the member address does not exist."}
                    else:
                        # The SQL function didn't execute successfully
                        logging.info("get_member_address SQL statement failed")
                        code = responses.CODE_INTERNAL_ERROR
                        message = { "message" : "Internal Server Error" }
                else : 
                    code = responses.MEMBER_DOESNT_EXIST_RESPONSE
                    message = {"message" : "This member does not exist"}
            else : 
                logging.info("member_exists_check SQL statement failed")
                code = responses.CODE_INTERNAL_ERROR
                message = {"message" : "Internal Server Error"}

    except Exception as e :
        logging.error("Exception occured while executing function: get-member-address\n" + traceback.format_exc())
        code = responses.CODE_INTERNAL_ERROR
        message = {"message":"Internal Server Error"}
    finally : 
        logging.info("Ended executing azure function: get-member-address")

        return func.HttpResponse(
                status_code=code,
                body=json.dumps(message, default=str),
                mimetype="application/json")
