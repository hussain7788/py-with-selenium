import logging
import os
import plaid
import base64
import socket
from azure.identity import ManagedIdentityCredential,DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,  EnvironmentCredential
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)

credentials = DefaultAzureCredential()

secret_client = SecretClient(vault_url=os.environ.get('KEY_VAULT'), credential=credentials)
# value = secret_client.get_secret('postgresPW').value

POSTGRESS_DB_PASSWORD = secret_client.get_secret('postgresPW').value
POSTGRESS_DB_NAME = secret_client.get_secret('postgresDb').value
POSTGRESS_DB_PORT = secret_client.get_secret('postgresPort').value
POSTGRESS_HOST = secret_client.get_secret('postgresHost').value
POSTGRESS_USER = secret_client.get_secret('postgresUser').value
DEMYST_URL = secret_client.get_secret('demyst-url').value
DEMYST_API_KEY = secret_client.get_secret('demyst-api-key').value
DEMYST_HOME_VALUE_ID = secret_client.get_secret('demyst-home-value-id').value
FINXACT_DSS_ID = secret_client.get_secret('finxact-dss-id').value
SELF_REPORTED_INCOME_TYPE = secret_client.get_secret('self-reported-income-type').value
client_id = secret_client.get_secret('plaid-client-id').value
secret = secret_client.get_secret('plaid-secret').value
plaid_broker_url = secret_client.get_secret('plaid-broker-url').value
plaid_link_url = secret_client.get_secret('plaid-link-url').value
space_id = secret_client.get_secret('contentfulSpaceId').value
access_token = secret_client.get_secret('contentfulAccessToken').value

# MORTGAGE: SUNWEST Credentials and URLS
SUNWEST_BASE_URL = secret_client.get_secret('sunwest-base-url').value
SUNWEST_USERNAME = secret_client.get_secret('sunwest-username').value
SUNWEST_PASSWORD = secret_client.get_secret('sunwest-password').value
MISMO_IMPORT_URL = SUNWEST_BASE_URL+"mismo/import?mismoType=blend"
MISMO_TOKEN_URL = SUNWEST_BASE_URL+"session"
LOAN_URL = SUNWEST_BASE_URL+"live/loan"
POST_LOAN_SEARCH = SUNWEST_BASE_URL+"live/loan/search"

# MORTGAGE: Email settings for sending disclosure documents
GLORIFI_EMAIL_HOST = secret_client.get_secret('glorifi-email-host').value
GLORIFI_EMAIL_FROM = secret_client.get_secret('glorifi-email-from').value
GLORIFI_EMAIL_SUBJECT = "#{number} - Disclosure Document"
GLORIFI_EMAIL_SUNWEST_UPLOAD_SUBJECT = "Sunwest MISMO file upload status"
GLORIFI_EMAIL_BODY = "Hi,\n\nPlease find the attached loan disclosure document.\n\n"
GLORIFI_EMAIL_SUNWEST_UPLOAD_STATUS_TO_MGR = ['kristie.szypula@glorifi.com']
# GLORIFI_EMAIL_SUNWEST_UPLOAD_STATUS_TO_MGR = ['jiffinjoachim.gomez@glorifi.com', 'nelson.chacko@glorifi.com']

# MORTGAGE: Currently Supported List of states which needs disclosure document
DISCLOSURE_SUPPORTED_STATES = ['SD', 'IA', 'ME', 'LA', 'MS', 'DE','VT']

# MORTGAGE: Blend MISMO API & Proxy Mortgage API
BLEND_MISMO_PROXY_URL = secret_client.get_secret('blend-mismo-proxy-url').value
PROXY_MORTGAGE_URL = secret_client.get_secret('proxy-mortgage-url').value
# BLEND_MISMO_PROXY_URL = "https://animo-testapimgmt.azure-api.net/blend/home-lending/applications/"
# PROXY_MORTGAGE_URL = "https://animo-testapimgmt.azure-api.net/data-services"
# PROXY_MORTGAGE_URL = "http://localhost:7075"


if 'sandbox' in plaid_link_url:
    plaid_host = plaid.Environment.Sandbox
elif 'development' in plaid_link_url:
    plaid_host = plaid.Environment.Development
elif 'production' in plaid_link_url:
    plaid_host = plaid.Environment.Production

BANKING_SUMMARY_INFO_MAPPING = {
    "savings": ["sav", "saving", "savings", "compounding-personal"],
    "cd": ["cd", "CD", "certificate of deposit", "Certificate of Deposit"],
    "checkings": ["dda", "checkings", "checking"],
    "credit_card": ["credit card"]
}

INSURANCE_HEADERS_INFO_MAPPING = {
    "home": ["home", "home owners", "condo", "renters", "rent", "home insurance", "condo insurance", "renters insurance"],
    "auto": ["auto insurance", "motorcycle insurance", "auto", "4 wheeler", "car owner", "2 wheeler", "autop"],
    "pet": ["pet insurance", "pet", "PET"],
    "umbrella": ["umbrella insurance", "PUMBR", "pumbr"]
}


ANI_REGEX_VERIFIER=r"^\+?[1-9]\d{1,14}$"
ANI_REGEX_ERROR_MSG=u'Ani number is not in E.164 format'

class Config:
    def __init__(self):
        self.__key_vault_url = secret_client.get_secret('KEYVAULT-URL-KAFKA').value
        self.__kafka_groupid_name = secret_client.get_secret('KAFKA-CONSUMER-GROUPID').value
        self.__environment_name = secret_client.get_secret('ENVIRONMENT-NAME-KAFKA').value
        self.__topic_name = secret_client.get_secret('KAFKA-TOPIC-NAME').value
        self.__secret_client = None
        self.configure_creditionals()
        self.log_environment_values()
        #os.makedirs(os.path.dirname('logs/'), exist_ok=True)
    
    def get_kafka_groupid_name(self):
        return self.__kafka_groupid_name

    def get_topic_name(self):
        return self.__topic_name


    def configure_creditionals(self):
        if self.__key_vault_url:
            try:
                if self.__environment_name == "local":
                    credentials =  DefaultAzureCredential(exclude_visual_studio_code_credential=True)
                else:
                    credentials = EnvironmentCredential()
                self.__secret_client = SecretClient(vault_url=self.__key_vault_url, credential=credentials)

            except Exception as error:
                logger.error(f"Error Occured when connecting with Azure Creditionals: {str(error)}") 
                raise Exception(error)
        else:
            logger.info(f"Missing Keyvault Url in Function App Environment.Please check Function App Configuration." )



    def log_environment_values(self):
        logger.info(f"""
        ************************************************************************************
                                        Settings.py

        Keyvault url is : {self.__key_vault_url}
        Environment Name is : {self.__environment_name}
        Topic Name is : {self.__topic_name}
        Host Name is : {socket.gethostname()}
        GROUP ID NAME: {self.get_kafka_groupid_name()}

        ************************************************************************************
        
        """)

    def get_azure_secret_client(self):
        return self.__secret_client

    def get_azure_keyvault_secret_value(self, keyvault_value):
        value = None
        try:
            if os.environ.get(keyvault_value):
                logger.info(f"{keyvault_value} Found in local environment")
                value = os.environ.get(keyvault_value)
            else:
                value  =  self.__secret_client.get_secret(keyvault_value).value
                os.environ[keyvault_value]=str(value)
                logger.info(f"{keyvault_value} Fetched from keyvault")
        except Exception as e:
            logger.error(f"Error Occured with Accessing keyvault secret with id - {keyvault_value}: {str(e)}")
            raise Exception(e)
        else:
            return  value
configure = Config()
