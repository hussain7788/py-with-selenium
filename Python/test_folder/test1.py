import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
sys.path.append(os.path.abspath(os.path.join('../assets-dev')))
sys.path.append(os.path.abspath(os.path.join("./glo_core_app_common")))
import logging
import json
import traceback
import azure.functions as func
from utils.constants import *
from utils.requests_validation import zipcode_validation
import zipcodes
from config_managemnt.string_table import ZIPCODE_VALIDATION_FAILED, ZIPCODE_MATCHING_FAILED
from gloripy.utils.http_response_handler import InternalServerError, Successful, Unauthorized, HTTPException, Successful, BadRequest
import gloripy.auth as Auth
from apiclient.exceptions import APIClientError
from gloripy.utils.context_logging.logger import initiate_context_logging


def main(req: func.HttpRequest, context) -> func.HttpResponse:
    
    '''Given zip code is validated using Google SDK to check if it is a validate US zip code.

    Args: 
        context : Object wrapping the context information of the http request like request id 
        req: Object wrapping the http request with zipcode

    Returns: Zipcode is valid or not valid. 
    '''
   
    try:
        initiate_context_logging(req, context)
        logging.info(f'Executing function: {func.Context.function_directory}')

        # get zip code
        zipcode = req.route_params.get('zipcode') 

        request_body = {'zipcode': zipcode}

        logging.info(f"python HTTP trigger function processed a request to validate zip code, Going to start Zipcode Validation, Request Body {request_body}.")

        req__val_res = zipcode_validation(request_body)
        result = {}
        result["is-valid"] = "false"
      
        if req__val_res['status_code'] == CODE_OK:
            logging.info(f"Validation response {req__val_res}")

            logging.info(f"Successfully validated Zipcode, Going to start matching zipcode {zipcode}.")

            res = zipcodes.matching(zipcode)

            try:
                res = res[0]
                logging.info(f"Successfully matched zipcode, Zipcode Matching Response {res}.")
                if  "country" in res:
                    if res['country'] == "US":
                        result["is-valid"] = "true"
            except:
                logging.error(f"{ZIPCODE_MATCHING_FAILED}, Zipcode Matching Response {res}")
        else:


        response={"success":SUCCESS_CODE,"data": result,
        "status": SUCCESS, "message": VALIDATION_SUCCESS}
        
        logging.info("Successfully recieved the response")
        response = Successful(data=response, message="Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))

    except Exception as e:
        logging.error("Error :" + traceback.format_exc())
        response = InternalServerError(message = str(e) + "\n" + "Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))

    finally:
        logging.info("Zip Code Validation Completed.\n" f"Response = {json.dumps(response.__dict__)}")
        return func.HttpResponse(json.dumps(response.__dict__), status_code=response.status_code, mimetype="application/json")
