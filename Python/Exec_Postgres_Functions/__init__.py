import logging
import azure.functions as func
import traceback
import json
from gloripy.utils.http_response_handler import InternalServerError, Successful, Unauthorized, HTTPException, Successful, BadRequest, NotFound
import gloripy.auth as Auth
import asyncio
from apiclient.exceptions import APIClientError
from src.fetch.savana import SavanaClient
from src.fetch.banking import BankingClient
from src.logic.database_calls import call_pg_function
from gloripy.utils.context_logging.logger import initiate_context_logging

def main(req: func.HttpRequest, context) -> func.HttpResponse:
    """ PLAID TRANSFER ACCOUNT POST
    Args:
        product

    Returns:
        HttpResponse
    """
    try:
        initiate_context_logging(req, context)
        logging.info(f'Executing function: {func.Context.function_directory}, Starting Token Validation.' )
        token = req.headers.get("Authorization", None)
        uuid = asyncio.run(Auth.validate_and_decode_auth_header(token))
        logging.info(f"Successfully Validated Token, mamber_id: {uuid}, Fetching Savana access token and customer token.")
        s_client = SavanaClient(token=token, req=req, context=context)
        logging.info(f"Fetched savana access token: {s_client.savanaAccessToken} and savana customer token: {s_client.customerToken}, Fetching Request body.")
        
        plaidObj = req.get_json()
        plaidToken = plaidObj["public_token"]
        accounts = plaidObj["accounts"]
        logging.info(f"Fetched Request Body, {req.get_json()}, Registering Linked Account.")
        b_client = BankingClient(s_client.customerToken,s_client.savanaAccessToken)
        responses = b_client.registerLinkedAccount(plaidToken, accounts)

        id_arr = ref_arr = raw_json_arr = status_arr =[]
    
        for response in responses:
            raw_json_arr.append(json.dumps(response))
            id_arr.append(response.get("_Id", ""))
            ref_arr.append(response.get("linkedAcct", {}).get("ref", ""))
            status_arr.append(response.get("status",""))
        
        logging.info(f'Registered Linked Account, Status: {status_arr}\n IDs: {id_arr}\n Ref: {ref_arr}\n Raw JSON: {raw_json_arr}\n Invoking Datahub Post Plaid Auth Accounts.')

        call_pg_function('datahub.post_plaid_auth_accounts', 
            [uuid, id_arr, ref_arr, status_arr, raw_json_arr])
        
        logging.info("Invoked Success.")
        response = Successful(data=responses, message="Successfully Fetched ,"+ str(req.url) + " with Invocation ID " + str(context.invocation_id))

    except APIClientError as e:
        logging.error("\n Error : fetching data from client" + traceback.format_exc())
        response = HTTPException(status_code=e.status_code, error_code=e.status_code, message=str(e) + "\n" + "Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))

    except Auth.TokenException as e:
        logging.error("Error : with authorization" + traceback.format_exc())
        response = Unauthorized(message = str(e) + "\n" + "Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))

    except ValueError as e:
        logging.error("Error : with authorization" + traceback.format_exc())
        response = BadRequest(message = str(e) + "\n" + "Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))

    except BadRequest as e:
        logging.error("Error :" + traceback.format_exc())
        response = BadRequest(message = str(e) + "\n" + "Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))
 
    except NotFound as e:
        logging.error("Error :" + traceback.format_exc())
        response = NotFound(message = str(e) + "\n" + "Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))

    except Exception as e:
        logging.error("Error :" + traceback.format_exc())
        response = InternalServerError(message = str(e) + "\n" + "Invocation of " + str(context.function_name) + " with Invocation ID " + str(context.invocation_id))

    finally:
        logging.info(f"{func.Context.function_directory} Request Complete.\n" f"Response = {json.dumps(response.__dict__)}")
        return func.HttpResponse(json.dumps(response.__dict__), status_code=response.status_code, mimetype="application/json")