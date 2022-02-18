import { loadStripe } from "@stripe/stripe-js";
//API Configuration - This must be same as the Django Backend Port

//Deployment - Always keep this version.
//export const __CLIENT_HOST = "www.cpasage.com/";
//export const HOSTNAME = "https://" + __CLIENT_HOST;
//export const WS_HOSTNAME = "wss://" + __CLIENT_HOST;

// Local: Uncomment this for local
export const __CLIENT_HOST = process.env.REACT_APP_API_HOST;

let httpPrefix = "http://";
let wsPrefix = "ws://";
if (process.env.REACT_APP_CONN_TYPE == "secure") {
    httpPrefix = "https://";
    wsPrefix = "wss://";
}
export const HOSTNAME = httpPrefix + __CLIENT_HOST;
export const WS_HOSTNAME = wsPrefix + __CLIENT_HOST;

export const CONFIG_ENDPOINT = HOSTNAME + "api/config/";

// This is where all the url constants are defined

//Authentication URLS
export const ADMIN_SIGNUP = "/admin_signup/";

export const G_SIGNIN = "/signin/";
export const LOGOUT = "/logout/";
export const G_INDEX = "/";
export const G_ABOUT_US = "/aboutus/";
export const G_FEATURES = "/features/";
export const G_PRICING = "/pricing/";
export const G_CONTACT_US = "/contactus/";
export const G_TERMS = "/terms/";
export const G_PRIVACY = "/privacy/";

export const BASE_ADMIN_HOME = "/home/";
export const ADMIN_HOME = BASE_ADMIN_HOME + ":adminCode/";

export const BASE_ADMIN_SIGNIN = "/signin/";
export const ADMIN_SIGNIN = BASE_ADMIN_SIGNIN + ":adminCode/";

export const BASE_ADMIN_ABOUTUS = "/admin_aboutus/";
export const ADMIN_ABOUTUS = BASE_ADMIN_ABOUTUS + ":adminCode/";

export const BASE_ADMIN_SERVICES = "/admin_services/";
export const ADMIN_SERVICES = BASE_ADMIN_SERVICES + ":adminCode/";

export const BASE_CLIENT_SIGNUP = "/signup/";
export const CLIENT_SIGNUP = BASE_CLIENT_SIGNUP + ":adminCode/";
export const REFER_CLIENT_SIGNUP = BASE_CLIENT_SIGNUP + ":adminCode/:userInfo/";

export const BASE_CLIENT_ACTIVATION = "/account_activation/";
export const CLIENT_ACTIVATION = BASE_CLIENT_ACTIVATION + ":adminCode/:adminId/:userId/";

export const BASE_RESET_PASSWORD = "/reset_password/";
export const RESET_PASSWORD = BASE_RESET_PASSWORD + ":adminCode/:accessMark/:accessId/";

export const BASE_CHANGE_PASSWORD = "/change_password/";
export const CHANGE_PASSWORD = BASE_CHANGE_PASSWORD + ":adminCode/";

export const FORGOT_PASSWORD = "/forgot_password/";

export const BASE_ADMIN_FORGOT_PASSWORD = "/forgot_password/";
export const ADMIN_FORGOT_PASSWORD = BASE_ADMIN_FORGOT_PASSWORD + ":adminCode/";

// Top Level Super Admin URLS
export const SUPER_ADMIN_DASHBOARD = "/sadashboard/";
export const SUPER_ADMIN_LEADS = "/saleads/";

// Top Level Admin URLS
export const ADMIN_DASHBOARD = "/dashboard/";
export const COMMON_TASK_LIST = "/workflow/";
export const COMMON_MANUAL_TASK_LIST = "/projects/";
export const ADMIN_CLIENT_ACTION = "/client/";
export const ADMIN_EMP_ACTION = "/team/";
export const ADMIN_INSIGHT = "/insight/";
export const ADMIN_BULK_MSG = "/bulk_msg/";
export const ADMIN_NOTIFICATIONS = "/notifications/";
export const ADMIN_SCHEDULER = "/appointments/";
export const ADMIN_SETTINGS = "/settings/";
export const ADMIN_PASSWORD_MANAGEMENT = "/passwordmanagement/";

export const USER_REFER_REVIEW = "/refer-review/";

export const TICKETS = "/tickets/";
export const BASE_TICKETS_DETAILS = "/ticketdetail/";
export const TICKETS_DETAILS = BASE_TICKETS_DETAILS + ":ticketId/";

export const BASE_MANUAL_TASK_DETAILS = "/project-dashboard/";
export const MANUAL_TASK_DETAILS = BASE_MANUAL_TASK_DETAILS + ":userId/:taskId/";

export const BASE_CONTACT_US = "/cpa-contact-us/";
export const CONTACT_US = BASE_CONTACT_US + ":code/";
export const REFER_CONTACT_US = BASE_CONTACT_US + ":code/:userInfo/";

export const BASE_PAY_INVOICE = "/pay/";
export const PAY_INVOICE = BASE_PAY_INVOICE + ":invoiceId/";

export const LEADS = "/leads/";

//Client Dashboard URLS
export const BASE_COMMON_CLIENT_DASHBOARD = "/client_dashboard/";
export const COMMON_CLIENT_DASHBOARD = BASE_COMMON_CLIENT_DASHBOARD + ":userId/";

//Client Dashboard URLS from Client View
export const CLIENT_DASHBOARD = "/user_dashboard/";
export const CLIENT_COMMUNICATION = "/user_communication/";
export const CLIENT_DOCUMENT = "/user_document/";
export const CLIENT_STATUS = "/user_status/";
export const CLIENT_BUSINESS = "/user_business/";
export const CLIENT_ORGANIZER = "/user_template/";
export const CLIENT_INVOICE = "/user_invoice/";
export const CLIENT_PROJECT = "/user_project/";
export const CLIENT_DEPENDENT = "/user_dependent/";

export const BASE_COMMON_EMP_DASHBOARD = "#";
export const COMMON_EMP_DASHBOARD = BASE_COMMON_EMP_DASHBOARD;

//Recep Specific Urls
export const RECEP_CLIENT_LIST = "/clients/";

export const HELLO_SIGN_CLIENT_ID = "b1d4cdc93c877524d43c052c5562c5b0";

//Stripe SDK Init
export const STRIPE_KEY = "pk_test_51JXHvDC2JFXQK27GcPoIpgNs4ExyyqxLD2PYyHCb6xS8cbDG7h3RyPBMQO2mhVNe8EhblG73jdnLRpnMEPXVTOjn003U7cJmuq"
export const stripePromise = loadStripe(STRIPE_KEY);

export const IS_GENERATE_IDS = false //This flag to be used to control generation of IDs for testing - Note: Production shouls ALWAYS be false