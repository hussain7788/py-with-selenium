from pm.test.test_data.test_data_class.test_data_tasks import *
from pm.test.test_data.test_data_class.test_data_admin import *
from pm.test.test_data.test_data_class.test_data_emp import *
from pm.test.test_data.test_data_class.test_data_client import *
from pm.test.test_data.test_data_class.test_data_admin_actions_team_client import *
from pm.test.test_data.test_data_class.test_data_admin_profile import *
from pm.test.test_data.test_data_class.test_data_admin_client_dashboard import *
from pm.test.test_data.test_data_class.test_data_tickets import *
from pm.test.test_data.test_data_class.test_data_notifications import *
from pm.test.test_data.test_data_class.test_data_insights_practice import *
from pm.test.test_data.test_data_class.test_data_insights_growth import *
from pm.test.test_data.test_data_class.test_data_insights_client import *
from pm.test.test_data.test_data_class.test_data_reset_password import *
from pm.test.test_data.test_data_class.test_data_appointment import *
from pm.test.test_data.test_data_class.test_data_update_client_profile import *
from pm.test.test_data.test_data_class.test_data_change_password import *

from pm.test.selenium_utility.sl_functions import *
import random
import pdb


file_name = []
growth_insight_count = 0
growth_insight_total_amount = 0
class test_data_gen():
    num_admins = None
    num_clients = None
    num_bns = None
    num_bns_file = None
    num_per_file = None
    num_rcp = None
    num_mgrs = None
    num_emps = None
    num_invoices =  None
    offset = None
    l_d_users = None
    ticket_test = None
    d_price_cal = None
    path = None

    def __init__(self, params = None, response = None):
        self.num_admins = params['num_admins']
        self.num_clients = params['num_clients']
        self.num_bns = params['num_bns']
        self.num_bns_files = params['num_bns_files']
        self.num_per_files = params['num_per_files']
        self.num_rcp = params['num_rcp']
        self.num_mgrs = params['num_mgrs']
        self.num_emps = params['num_emps']
        self.num_invoices = params['num_invoices']
        self.offset = params['offset']
        self.d_price_cal = params['d_price_cal']
        self.l_d_users = []
        self.ticket_test = params['ticket_test']
        self.appointment_test = params['appointment_test']
        self.client_team_action_test = params['client_team_action_test']
        global d_config
        global d_config_ticket
        global d_config_profile
        d_config['path'] = params['path']
        d_config_ticket['path'] = params['path']
        d_config_profile = params['path']

    def set_base_data(self):
        num_admins = self.num_admins
        num_clients = self.num_clients
        num_bns = self.num_bns
        num_bns_files = self.num_bns_files
        num_per_files = self.num_per_files
        num_rcp = self.num_rcp
        num_mgrs = self.num_mgrs
        num_emps = self.num_emps
        num_invoices = self.num_invoices
        offset = self.offset
        d_price_cal = self.d_price_cal
        path = self.path
        ticket_test = self.ticket_test
        client_team_action_test = self.client_team_action_test

        for admin_num in range(offset, offset + num_admins, 1):
            d_users = {
                'd_special_admin' : {},
                'd_special_mgr' : {},
                'd_special_client' : {},
                'l_d_special_rcp': [],
                'l_d_appointments':[],
                'd_admin': {},
                'd_super_admin':{},
                'd_super_admin_emp':{},
                'l_d_clients': [],
                'l_d_rcp': [],
                'l_d_mgrs': [],
                'l_d_emps': [],
                'l_d_doc': [],
                'l_d_msgs': [],
                'l_d_unassigned_tasks': [],
                'l_d_due_date_tasks': [],
                'l_d_assigned_tasks': [],
                'l_d_mgr_review_tasks': [],
                'l_d_admin_review_tasks': [],
                'l_d_client_review_tasks': [],
                'l_d_efile_auth_tasks': [],
                'l_d_efiled_tasks': [],
                'l_d_closed_tasks': [],
                'l_d_clients_delete': [],
                'l_d_mgrs_delete':[],
                'l_d_client_actions' : [],
                'l_d_team_actions' : [],
                'd_price_cal' : {},
                'l_d_price_est' : [],
                'd_client_links' : [],
                'l_invoice' : [],
                'l_invoice_verify' : [],
                'l_todo_tasks' : [],
                'l_auto_todo' : [],
                'l_access_settings' : [],
                'l_verify_access_settings' : [],
                'l_d_insight_practice' : [],
                'l_d_insight_client' : [],
                'l_d_insight_growth' : [],
                'l_notifi_count' : [],
                'l_notifi_msg_count' : [],
                'l_d_efile_auth_sendReminder_tasks': [],
                'l_d_update_client_profile': [],
                'l_d_ticket':[],
                'd_reset_password':{},
            }
            l_team_emails = list()
            l_client_emails = list()
            l_emps_firstname = list()
            l_client_full_names = list()
            l_auto_todo_count = list()
            l_d_b_status = [{'Initial': 0},{'Admin Review': 0}, {'Info Pending': 0}, {'Client Review': 0}, {'Efile Auth': 0}, {'Efiled': 0}, {'Closed': 0}],
            l_d_p_status = [{'Initial': 0},{'Admin Review': 0}, {'Info Pending': 0}, {'Client Review': 0}, {'Efile Auth': 0}, {'Efiled': 0}, {'Closed': 0}],
            self.create_admin_data(d_users, admin_num, l_emps_firstname)
            self.create_special_admin_data(d_users)
            self.create_special_mgr_data(d_users)
            self.create_special_client_data(d_users)
            self.create_super_admin_data(d_users)
            self.create_super_admin_emp_data(d_users)
            self.create_price_cal_data(d_users, d_price_cal)
            self.create_reset_password_data(d_users)

            if self.ticket_test == 'yes':
                self.create_data_tickets(d_users, admin_num)

            if self.appointment_test == 'yes':
                self.create_test_data_appointment(d_users)
            for client_num in range(1, num_clients + 1, 1):
                self.create_client_data(d_users, admin_num, client_num, num_bns, num_bns_files, num_per_files, d_price_cal, l_client_emails, l_client_full_names, l_auto_todo_count, num_invoices)

            for rcp_num in range(1, num_rcp + 1, 1):
                self.create_rcp_data(d_users, admin_num, rcp_num)

            for mgr_num in range(1, num_mgrs + 1, 1):
                self.create_mgr_data(d_users, admin_num, mgr_num, num_emps, l_team_emails, l_emps_firstname)
                self.create_unassigned_task_data(d_users, admin_num, mgr_num, num_bns, l_d_b_status, l_d_p_status)
                self.create_due_date_task_data(d_users, admin_num, mgr_num, num_bns)
                self.create_assigned_task_data(d_users, admin_num, mgr_num, num_bns)

                self.create_emp_doc_actions(d_users, admin_num, mgr_num, num_bns, num_bns_files, num_per_files)
                self.create_mgr_review_task_data(d_users, admin_num, mgr_num, num_bns)

                self.create_admin_review_task_data(d_users, admin_num, mgr_num, num_bns, l_d_b_status, l_d_p_status)
                self.create_profile_settings_data(d_users, mgr_num)

            self.create_notification_data(d_users, l_client_full_names, l_auto_todo_count)
            self.create_special_rcp_data(d_users)
            self.test_data_insights_unassign_practice(d_users, l_d_b_status, l_d_p_status)
            self.test_data_insights_adminReview_practice(d_users, l_d_b_status, l_d_p_status)
            self.create_client_data_delete(d_users, admin_num, client_num, l_client_emails)
            self.create_mgr_data_delete(d_users, admin_num, mgr_num, l_team_emails)
            if self.client_team_action_test == 'yes':
                self.create_data_admin_client_actions(d_users, l_client_emails)
                self.create_data_admin_team_actions(d_users, l_team_emails)

            self.create_client_review_task_data(d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status)
            self.test_data_insights_clientReview_practice(d_users, l_d_b_status, l_d_p_status)
            self.create_data_messages(d_users)
            self.create_efile_auth_task_data(d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status)
            self.test_data_insights_efileAuth_practice(d_users, l_d_b_status, l_d_p_status)
            self.create_efile_auth_sendReminder_task_data(d_users, admin_num, num_bns, num_clients)

            self.create_efiled_task_data(d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status)
            self.test_data_insights_efiled_practice(d_users, l_d_b_status, l_d_p_status)
            self.create_closed_task_data(d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status)
            self.test_data_insights_closed_practice(d_users, l_d_b_status, l_d_p_status)
            self.test_data_insights_practice(d_users, l_emps_firstname)
            self.test_data_insights_client(d_users)
            self.test_data_insight_growth(d_users, l_client_full_names, growth_insight_count, growth_insight_total_amount)
            self.l_d_users.append(d_users)

    def get_base_data(self):
        return self.l_d_users

    def create_admin_data(self, d_users, admin_num, l_emps_firstname):
        first_name = str("admin" + str(admin_num).zfill(2))
        l_emps_firstname.append(first_name)
        last_name = "lname"
        company_name = str("CPA Sage " + str(admin_num).zfill(2))
        email = str(first_name + "." + last_name + "@cpa.com")
        phone = "123-456-7890"
        password = "123"
        admin_obj = test_data_admin(first_name, last_name, company_name, email, phone, password)
        d_users['d_admin'] = admin_obj

    def create_super_admin_data(self, d_users):
        first_name = "super_admin",
        last_name = "last",
        email = "super_admin.last@admin.com",
        company_name = "yours_efficiently",
        phone = '123456789',
        password = "123",
        admin_obj = test_data_admin(first_name, last_name, company_name, email, phone, password)
        d_users['d_super_admin'] = admin_obj

    def create_super_admin_emp_data(self, d_users):
        first_name = "super_admin_emp",
        last_name = "last",
        email = "super_admin_emp.last@adminemp.com",
        company_name = "yours_efficiently",
        phone = '123456789',
        password = "123",
        admin_obj = test_data_admin(first_name, last_name, company_name, email, phone, password)
        d_users['d_super_admin_emp'] = admin_obj

    def create_special_admin_data(self, d_users):
        first_name = "Sarah",
        last_name = "Walker",
        email = "sarah.walker@cpa.com",
        company_name = "yours_efficiently",
        phone = '123456789',
        password = "123",
        admin_obj = test_data_admin(first_name, last_name, company_name, email, phone, password)
        d_users['d_special_admin'] = admin_obj

    def create_client_data(self, d_users, admin_num, client_num, num_bns, num_bns_files, num_per_files, d_price_cal, l_client_emails, l_client_full_names, l_auto_todo_count, num_invoices):
        first_name = str(str(admin_num).zfill(2) + "_client" + str(client_num).zfill(2))
        last_name = "lname"
        client_full_name = str(first_name + str(' ') + last_name)
        l_client_full_names.append(client_full_name)
        email = str(first_name + "." + last_name + "@client.com")
        l_client_emails.append(email)
        phone = "123-456-7890"
        password = "123"
        l_bns = []
        l_file_dtls = []
        l_bns_names = []

        for bns_num in range(1, num_bns + 1, 1):
            business_name = str(str(admin_num).zfill(2) + "_" + str(client_num).zfill(2) + "_business" + str(bns_num).zfill(2))
            l_bns_names.append(business_name)
            self.create_c_bns_data(l_bns, business_name)
            self.create_c_bns_files(d_users, l_file_dtls, business_name, bns_num, num_bns_files, d_price_cal)

        self.create_c_per_files(d_users, l_file_dtls, num_per_files, d_price_cal)

        client_obj = test_data_client(first_name, last_name, email, phone, password, l_bns, l_file_dtls)
        d_users['l_d_clients'].append(client_obj)

        self.create_auto_todo_data(d_users, l_bns_names, l_auto_todo_count)
        self.create_update_client_profile_data(d_users, client_num)
        self.create_invoice_data(d_users, num_invoices)
        self.create_todo_task_data(d_users)

    def create_client_data_delete(self, d_users, admin_num, client_num, l_client_emails):
        first_name = str(str(admin_num).zfill(2) + "_client" + str(client_num).zfill(2))
        last_name = "delete"
        email = str(first_name + "." + last_name + "@client.com")
        l_client_emails.append(email)
        phone = "123-456-7890"
        password = "123"

        client_obj = test_data_client(first_name, last_name, email, phone, password, l_bns = None, l_file_dtls = None)
        d_users['l_d_clients_delete'].append(client_obj)

    def create_special_client_data(self, d_users):
        first_name = "Percy",
        last_name = "Jackson",
        email = "percy.jackson@client.com",
        phone = '123456789',
        password = "123",

        client_obj = test_data_client(first_name, last_name, email, phone, password, l_bns = None, l_file_dtls = None)
        d_users['d_special_client'] = client_obj

    def create_c_bns_data(self, l_bns, business_name):
        business_type = "LLP"
        bns_inc_state = "CA"
        business_inco_date = "01012020"
        bk_frequency = "Monthly"
        pr_frequency = "Bi-Monthly"
        st_frequency = "Quarterly"
        tp_checkbox = True
        bns_obj = test_data_business(business_name, business_type, bns_inc_state, business_inco_date,
                                        bk_frequency, pr_frequency, st_frequency, tp_checkbox)
        l_bns.append(bns_obj)

    def create_auto_todo_data(self, d_users, l_bns_names, l_auto_todo_count):
        for bns_name in l_bns_names:
            todo_task1 = str(str(bns_name) + '-' + 'Payroll')
            todo_task2 = str(str(bns_name) + '-' + 'Tax Planning')
            todo_task3 = str(str(bns_name) + '-' + 'Sales Tax')
            todo_task4 = str(str(bns_name) + '-' + 'Book Keeping')

            l_auto_todo_ids = [todo_task1, todo_task2, todo_task3, todo_task4]
            l_auto_todo_count.append(len(l_auto_todo_ids))

            # validate obj
            id_obj = test_data_admin_client_dashboard(l_todo_task_names= l_auto_todo_ids)
            d_users['l_auto_todo'].append(id_obj)

    def create_c_bns_files(self, d_users, l_file_dtls, business_name, bns_num, num_bns_files, d_price_cal):
        l_files = []
        est_price = 0

        tab_name = "BusinessTab"
        sub_tab = "fromClient"
        client_login_access = True
        tax_year = "2019"
        bns_name = business_name
        document_source = "Received from Client"

        for file_num in range(1, num_bns_files + 1,):
            file_name = str(str(bns_num).zfill(2) + "bns_w2_" + str(file_num) + ".pdf")
            file_type = 'W-2'
            file_obj = test_data_file(file_name, file_type)
            l_files.append(file_obj)
            est_price = est_price + d_price_cal[file_type]

        # upload files
        file_dtl_obj = test_data_upload_files(tab_name, sub_tab, client_login_access, tax_year, document_source, bns_name, l_files)
        l_file_dtls.append(file_dtl_obj)
        # price est
        if len(d_users['l_d_price_est']) == 0 or len(d_users['l_d_price_est']) == 2:
            price_obj1 = test_data_price_est(tab_name = tab_name, year = tax_year, bns_name = bns_name, estimated_pr = est_price)
            d_users['l_d_price_est'].append(price_obj1)

    def create_c_per_files(self, d_users, l_file_dtls, num_per_files, d_price_cal):
        l_files = []
        est_price = 0

        tab_name = "PersonalTab"
        sub_tab = "fromClient"
        client_login_access = True
        tax_year = "2019"
        bns_name = None
        document_source = "Received from Client"

        for file_num in range(1, num_per_files + 1,):
            file_name = str("per" + "_" +  "w2" + "_" + str(file_num) + ".pdf" )
            file_type = 'W-2'
            file_obj = test_data_file(file_name, file_type)
            l_files.append(file_obj)
            est_price = est_price + int(d_price_cal[file_type])

        # upload files
        file_dtl_obj = test_data_upload_files(tab_name, sub_tab, client_login_access, tax_year, document_source, bns_name, l_files)
        l_file_dtls.append(file_dtl_obj)
        # price est
        price_obj1 = test_data_price_est(tab_name= tab_name, year=tax_year, estimated_pr=est_price)
        d_users['l_d_price_est'].append(price_obj1)

    def create_price_cal_data(self, d_users, d_price_cal):

        price_cal_obj = test_data_admin_profile(d_price_cal=d_price_cal,)
        d_users['d_price_cal'] = price_cal_obj

    def create_todo_task_data(self, d_users):
        l_todo_tasks = []
        due_date = "08012020"
        todo_task = "task1"
        todo_count = 0
        if todo_task :
            todo_count += 1
            l_todo_tasks.append(todo_count)

    # todo task obj
        todo_task_obj = test_data_admin_client_dashboard(todoDueDate = due_date, todoTask = todo_task, l_todo_task_names = [todo_task])
        d_users['l_todo_tasks'].append(todo_task_obj)
        return l_todo_tasks

    def create_update_client_profile_data(self, d_users, client_num):
        phone = '123-456-7890'
        spouse_first_name = str('Spouse' + str(client_num).zfill(2))
        spouse_last_name = str('Lname' + str(client_num).zfill(2))
        spouse_email = str(spouse_first_name.lower() + "." + spouse_last_name.lower() + "@spouse.com")
        spouse_phone = '987-654-3210'
        update_profile_obj = test_data_update_profile(phone = phone, spouse_first_name = spouse_first_name, spouse_last_name = spouse_last_name, spouse_email = spouse_email, spouse_phone = spouse_phone)
        d_users['l_d_update_client_profile'].append(update_profile_obj)

    def create_invoice_data(self, d_users, num_invoices):
        print("num_invoices", num_invoices)
        for invoice in range(1, num_invoices + 1):
            desc = str("desc" + str(invoice))
            qty = "1"
            price = str(invoice)
            global growth_insight_count
            global growth_insight_total_amount
            growth_insight_count = growth_insight_count + int(qty) #(0+1 + 1 + 1 + 1 = 4)
            growth_insight_total_amount = growth_insight_total_amount + int(price) #(0+1 + 2 + 1 + 2 = 6)

            if len(d_users['l_invoice']) == num_invoices:
                continue
            else:
                # add invoice
                invoice_obj1 = test_data_invoice(l_descs = [desc], l_qtys = [qty], l_prices = [price])
                d_users['l_invoice'].append(invoice_obj1)
                # invoice verify
                invoice_verify_obj = test_data_invoice(l_prices = [price])
                d_users['l_invoice_verify'].append(invoice_verify_obj)

    def create_rcp_data(self, d_users, admin_num, rcp_num):
        rcp_first_name = str(str(admin_num).zfill(2) + "_rcp" + str(rcp_num).zfill(2))
        rcp_last_name = "lname"
        email = str(rcp_first_name + "." + rcp_last_name + "@mgr.com")
        phone = "123-456-7890"
        password = "123"
        emp_type = "Front Office"
        emp_obj = test_data_emp(rcp_first_name, rcp_last_name, email, phone, password, emp_type, None)
        d_users['l_d_rcp'].append(emp_obj)

    def create_special_rcp_data(self, d_users):
        rcp_first_name = 'Recp'
        rcp_last_name = 'Nist'
        email = 'recp.nist@recp.com'
        phone = '123456789'
        password = "123"
        emp_type = "Front Office"
        rcp_obj = test_data_emp(first_name = rcp_first_name, last_name = rcp_last_name, email = email, phone = phone, password = password, emp_type = emp_type, manager = None)
        d_users['l_d_special_rcp'].append(rcp_obj)

    def create_mgr_data(self, d_users, admin_num, mgr_num, num_emps, l_team_emails, l_emps_firstname):
        mgr_first_name = str(str(admin_num).zfill(2) + "_mgr" + str(mgr_num).zfill(2))
        l_emps_firstname.append(mgr_first_name)
        mgr_last_name = "lname"
        email = str(mgr_first_name + "." + mgr_last_name + "@mgr.com")
        l_team_emails.append(email)
        phone = "123-456-7890"
        password = "123"
        emp_type = "Team Manager"
        emp_obj = test_data_emp(mgr_first_name, mgr_last_name, email, phone, password, emp_type, None)
        d_users['l_d_mgrs'].append(emp_obj)
        for emp_num in range(1, num_emps + 1, 1):
            self.create_emp_data(d_users, admin_num, mgr_num, emp_num, mgr_first_name, mgr_last_name, l_team_emails)

    def create_emp_data(self, d_users, admin_num, mgr_num, emp_num, mgr_first_name, mgr_last_name, l_team_emails):
        first_name = str(str(admin_num).zfill(2) + "_" + str(mgr_num).zfill(2) + "_emp" + str(emp_num).zfill(2))
        last_name = "lname"
        email = str(first_name + "." + last_name + "@emp.com")
        l_team_emails.append(email)
        phone = "123-456-7890"
        password = "123"
        emp_type = "Team Member"
        manager = str(mgr_first_name + " " + mgr_last_name)
        emp_obj = test_data_emp(first_name, last_name, email, phone, password, emp_type, manager)
        d_users['l_d_emps'].append(emp_obj)


    def create_mgr_data_delete(self, d_users, admin_num, mgr_num, l_team_emails):
        mgr_first_name = str(str(admin_num).zfill(2) + "_mgr" + str(mgr_num).zfill(2))
        mgr_last_name = "delete"
        email = str(mgr_first_name + "." + mgr_last_name + "@mgr.com")
        l_team_emails.append(email)
        phone = "123-456-7890"
        password = "123"
        emp_type = "Team Manager"
        emp_obj = test_data_emp(mgr_first_name, mgr_last_name, email, phone, password, emp_type, None)
        d_users['l_d_mgrs_delete'].append(emp_obj)

    def create_special_mgr_data(self, d_users):
        mgr_first_name = "John",
        mgr_last_name = "Casey",
        email = "john.casey@manager.com",
        phone = '123456789',
        password = "123",
        emp_type = "Team Manager"
        emp_obj = test_data_emp(mgr_first_name, mgr_last_name, email, phone, password, emp_type, None)
        d_users['d_special_mgr'] = emp_obj

    def create_test_data_appointment(self, d_users):
        appointment_data_obj = test_data_appointment(   name = 'appointment1',
                                                        email = 'percy.jackson@client.com',
                                                        hostName  = 'John Casey',
                                                        duration = '30 minutes',
                                                        # startTime = startTime,
                                                        date = '04/04/2020',
                                                        time = '02:02PM',
                                                        assert_result = True,
                                                        )
        d_users['l_d_appointments'].append(appointment_data_obj)

        appointment_details_data_obj = test_data_appointment( name = 'appointment1',
                                                            duration = '30 minutes',
                                                            # date = '12/31/2020',
                                                            date = '12/12/2020',
                                                            time = '04:32PM',
                                                            # action = 'yes',
                                                            # join_meetings = "yes",
                                                            # delete = "delete",
                                                            assert_result = True,
                                                            )
        d_users['l_d_appointments'].append(appointment_details_data_obj)

        appointment_details_data_obj = test_data_appointment( name = 'appointment1',
                                                            # duration = '30 minutes',
                                                            # date = '12/31/2020',
                                                            # time = '04:32PM',
                                                            action = 'yes',
                                                            # join_meetings = "yes",
                                                            # delete = "delete",
                                                            assert_result = True,
                                                            )
        d_users['l_d_appointments'].append(appointment_details_data_obj)

        appointment_details_data_obj = test_data_appointment( name = 'appointment1',
                                                            # duration = '30 minutes',
                                                            # date = '12/31/2020',
                                                            # time = '04:32PM',
                                                            action = 'yes',
                                                            join_meetings = "yes",
                                                            # delete = "delete",
                                                            assert_result = True,
                                                            )
        d_users['l_d_appointments'].append(appointment_details_data_obj)

        appointment_details_data_obj = test_data_appointment( name = 'appointment1',
                                                            # duration = '30 minutes',
                                                            # date = '12/31/2020',
                                                            # time = '04:32PM',
                                                            # action = 'yes',
                                                            # join_meetings = "yes",
                                                            delete = "delete",
                                                            assert_result = False,
                                                            )
        d_users['l_d_appointments'].append(appointment_details_data_obj)


    def create_data_admin_team_actions(self, d_users, l_team_emails):
        team_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = l_team_emails[-2:],
                                                                action = 'actInactivateBtn',
                                                                )
        d_users['l_d_team_actions'].append(team_action_data_obj)

        team_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = l_team_emails[-2:],
                                                                action = 'archiveBtn',
                                                                )
        d_users['l_d_team_actions'].append(team_action_data_obj)

        team_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = [l_team_emails[-1]],
                                                                action = 'deleteBtn',
                                                                )
        d_users['l_d_team_actions'].append(team_action_data_obj)

        team_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = [l_team_emails[-2]],
                                                                action = 'arcInactivateBtn',
                                                                )
        d_users['l_d_team_actions'].append(team_action_data_obj)

        team_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = [l_team_emails[-2]],
                                                                action = 'activateBtn',
                                                                )
        d_users['l_d_team_actions'].append(team_action_data_obj)

    def create_data_admin_client_actions(self, d_users, l_client_emails):
        client_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = l_client_emails[-2:],
                                                                action = 'actInactivateBtn',
                                                                )
        d_users['l_d_client_actions'].append(client_action_data_obj)

        client_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = l_client_emails[-2:],
                                                                action = 'archiveBtn',
                                                                )
        d_users['l_d_client_actions'].append(client_action_data_obj)
        client_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = [l_client_emails[-1]],
                                                                action = 'deleteBtn',
                                                                )
        d_users['l_d_client_actions'].append(client_action_data_obj)


        client_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = [l_client_emails[-2]],
                                                                action = 'arcInactivateBtn',
                                                                )
        d_users['l_d_client_actions'].append(client_action_data_obj)

        client_action_data_obj = test_data_team_n_client_actions(
                                                                l_emails = [l_client_emails[-2]],
                                                                action = 'activateBtn',
                                                                )
        d_users['l_d_client_actions'].append(client_action_data_obj)

    def create_emp_doc_actions(self, d_users, admin_num, mgr_num, num_bns, num_bns_files, num_per_files):
        client_name = d_users['l_d_clients'][mgr_num - 1].get_client_full_name()
        bns_name = None
        tab_name = "PersonalTab"
        sub_tab = "fromClient"
        tax_year = "2019"
        year = "2019"
        file_names = []
        for file_num in range(1, num_per_files + 1, 1):
            file_name = str("per_w2_" + str(file_num) + ".pdf")
            file_names.append(file_name)
        doc_obj = test_data_doc_actions(client_name, bns_name, tab_name, sub_tab, tax_year, file_names, year)
        d_users['l_d_doc'].append(doc_obj)

        for bns_num in range (1, num_bns + 1, 1):
            bns_name = str(str(admin_num).zfill(2) + "_" + str(mgr_num).zfill(2) + "_business" + str(bns_num).zfill(2))
            tab_name = "BusinessTab"
            file_names = []
            for file_num in range(1, num_bns_files + 1, 1):
                file_name = str(str(bns_num).zfill(2) + "bns_w2_" + str(file_num) + ".pdf")
                file_names.append(file_name)
            doc_obj = test_data_doc_actions(client_name, bns_name, tab_name, sub_tab, tax_year, file_names, year)
            d_users['l_d_doc'].append(doc_obj)

    def create_unassigned_task_data(self, d_users, admin_num, mgr_num, num_bns, l_d_b_status, l_d_p_status):
        sub_menu_option = 'unassignedTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = None
        action = 'assign'
        client_team_member = d_users['l_d_mgrs'][mgr_num - 1].get_full_name()
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = True
        #Unassigned Personal Task
        tab_name = 'personalTab'
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_unassigned_tasks'].append(admin_task_obj)
        l_d_p_status[0][0]['Initial'] += 1

        #Unassigned Business Task
        tab_name = 'businessTab'
        l_client_name = []
        l_year = []
        l_client_bns = []
        for bns_num in range (1, num_bns + 1, 1):
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()
            l_d_b_status[0][0]['Initial'] += 1

        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)

        d_users['l_d_unassigned_tasks'].append(admin_task_obj)

    def test_data_insights_unassign_practice(self, d_users, l_d_b_status, l_d_p_status):
        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Initial':l_d_p_status[0][0]['Initial']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Initial':l_d_b_status[0][0]['Initial']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

    def create_assigned_task_data(self, d_users, admin_num, mgr_num, num_bns):
        sub_menu_option = 'teamTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = "Assigned"
        action = 'assign'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = True

        #assigned Personal Task
        tab_name = 'personalTab'
        client_team_member = d_users['l_d_emps'][2*(mgr_num - 1)].get_full_name()
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        admin_task_obj = test_data_task(sub_menu_option = sub_menu_option, filter_year = filter_year, tab_name = tab_name, filter_status = filter_status, action = action,
                                        client_team_member = client_team_member, l_client_name = l_client_name, l_year = l_year, l_client_bns = l_client_bns, assert_result= assert_result)
        d_users['l_d_assigned_tasks'].append(admin_task_obj)

        #assigned Business Task
        tab_name = 'businessTab'
        client_team_member = d_users['l_d_emps'][2*(mgr_num - 1) + 1].get_full_name()
        l_client_name = []
        l_year = []
        l_client_bns = []
        for bns_num in range (1, num_bns + 1, 1):
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()

        admin_task_obj = test_data_task(sub_menu_option = sub_menu_option, filter_year = filter_year, tab_name = tab_name, filter_status = filter_status, action = action,
                                        client_team_member = client_team_member, l_client_name = l_client_name, l_year = l_year, l_client_bns = l_client_bns, assert_result= assert_result)
        d_users['l_d_assigned_tasks'].append(admin_task_obj)

    def create_due_date_task_data(self, d_users, admin_num, mgr_num, num_bns):
        sub_menu_option = 'teamTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = "Assigned"
        client_team_member = None
        action = None
        l_client_name = []
        l_year = []
        due_date = '05/12/2020'
        msg = 'new due date'
        l_client_bns = None
        assert_result = True

        #due date Personal Task
        tab_name = 'personalTab'
        # client_team_member = d_users['l_d_emps'][2*(mgr_num - 1)].get_full_name()
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        admin_task_obj = test_data_task(sub_menu_option = sub_menu_option, filter_year = filter_year, tab_name = tab_name, filter_status = filter_status, action = action,
                                        client_team_member = client_team_member, l_client_name = l_client_name, l_year = l_year, l_client_bns = l_client_bns, assert_result = assert_result, due_date = due_date, msg = msg)
        d_users['l_d_due_date_tasks'].append(admin_task_obj)
        #due date Business Task
        tab_name = 'businessTab'
        l_client_name = []
        l_year = []
        l_client_bns = []
        for bns_num in range (1, num_bns + 1, 1):
            l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()

        admin_task_obj = test_data_task(sub_menu_option = sub_menu_option, filter_year = filter_year, tab_name = tab_name, filter_status = filter_status, action = action,
                                        client_team_member = client_team_member, l_client_name = l_client_name, l_year = l_year, l_client_bns = l_client_bns, assert_result= assert_result, due_date = due_date, msg = msg)
        d_users['l_d_due_date_tasks'].append(admin_task_obj)


    def create_mgr_review_task_data(self, d_users, admin_num, mgr_num, num_bns):
        sub_menu_option = 'teamTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = "In Progress"
        action = 'managerReview'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = False

        #assigned Personal Task
        tab_name = 'personalTab'
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_mgr_review_tasks'].append(admin_task_obj)

        #assigned Business Task
        tab_name = 'businessTab'
        l_client_name = []
        l_year = []
        l_client_bns = []
        for bns_num in range (1, num_bns + 1, 1):
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()

        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_mgr_review_tasks'].append(admin_task_obj)

    def create_admin_review_task_data(self, d_users, admin_num, mgr_num, num_bns, l_d_b_status, l_d_p_status):
        sub_menu_option = 'reviewTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = "In Progress"
        action = 'adminReview'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = False

        #assigned Personal Task
        tab_name = 'personalTab'
        l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
        l_year.append('2019')
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_admin_review_tasks'].append(admin_task_obj)
        l_d_p_status[0][1]['Admin Review'] += 1

        #assigned Business Task
        tab_name = 'businessTab'
        l_client_name = []
        l_year = []
        l_client_bns = []
        for bns_num in range (1, num_bns + 1, 1):
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][mgr_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][mgr_num - 1].get_c_bns_names()
            l_d_b_status[0][1]['Admin Review'] += 1

        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_admin_review_tasks'].append(admin_task_obj)

    def test_data_insights_adminReview_practice(self, d_users, l_d_b_status, l_d_p_status):
        obj_data_insights_practice = Test_data_insights_practice(
                                                                # l_d_status = [{'Initial': 0},{'Admin Review': 0}, {'Info Pending': 0}, {'Client Review': 0}, {'Efile Auth': 0}, {'Efiled': 0}, {'Closed': 2}],
                                                                # l_d_status = list().append(l_d_p_status[0]),
                                                                l_d_status = [{'Admin Review':l_d_p_status[0][1]['Admin Review']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Admin Review':l_d_b_status[0][1]['Admin Review']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

    def create_client_review_task_data(self, d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status):
        sub_menu_option = 'reviewTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = None
        action = 'clientReview'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = True

        #assigned Personal Task
        tab_name = 'personalTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_d_p_status[0][3]['Client Review'] += 1
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_client_review_tasks'].append(admin_task_obj)

        #assigned Business Task
        tab_name = 'businessTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name = []
            l_year = []
            l_client_bns = []
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
            admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                            client_team_member, l_client_name, l_year, l_client_bns, assert_result)
            d_users['l_d_client_review_tasks'].append(admin_task_obj)
            l_d_b_status[0][3]['Client Review'] += 2


    def test_data_insights_clientReview_practice(self, d_users, l_d_b_status, l_d_p_status):
        obj_data_insights_practice = Test_data_insights_practice(
                                                                # l_d_status = [{'Initial': 0},{'Admin Review': 0}, {'Info Pending': 0}, {'Client Review': 0}, {'Efile Auth': 0}, {'Efiled': 0}, {'Closed': 2}],
                                                                # l_d_status = list().append(l_d_p_status[0]),
                                                                l_d_status = [{'Client Review':l_d_p_status[0][3]['Client Review']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Client Review':l_d_b_status[0][3]['Client Review']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

    def create_efile_auth_task_data(self, d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status):
        sub_menu_option = 'clientTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = 'Client Review'
        action = 'efileAuth'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = True

        #assigned Personal Task
        tab_name = 'personalTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_d_p_status[0][4]['Efile Auth'] += 1
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_efile_auth_tasks'].append(admin_task_obj)

        #assigned Business Task
        tab_name = 'businessTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name = []
            l_year = []
            l_client_bns = []
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
            admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                            client_team_member, l_client_name, l_year, l_client_bns, assert_result)
            d_users['l_d_efile_auth_tasks'].append(admin_task_obj)
            l_d_b_status[0][4]['Efile Auth'] += 2

    def test_data_insights_efileAuth_practice(self, d_users, l_d_b_status, l_d_p_status):
        obj_data_insights_practice = Test_data_insights_practice(
                                                                # l_d_status = [{'Initial': 0},{'Admin Review': 0}, {'Info Pending': 0}, {'Client Review': 0}, {'Efile Auth': 0}, {'Efiled': 0}, {'Closed': 2}],
                                                                # l_d_status = list().append(l_d_p_status[0]),
                                                                l_d_status = [{'Efile Auth':l_d_p_status[0][4]['Efile Auth']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Efile Auth':l_d_b_status[0][4]['Efile Auth']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

    def create_efile_auth_sendReminder_task_data(self, d_users, admin_num, num_bns, num_clients):
        sub_menu_option = 'clientTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = 'Efile Auth'
        action = 'sendReminder'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = True
        l_client_emails = []
        #assigned Personal Task
        tab_name = 'personalTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_client_emails.append(d_users['l_d_clients'][client_num - 1].get_client_email())
            l_year.append('2019')
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result, l_client_emails)
        d_users['l_d_efile_auth_sendReminder_tasks'].append(admin_task_obj)

        #assigned Business Task
        tab_name = 'businessTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name = []
            l_year = []
            l_client_bns = []
            l_client_emails = []
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_client_emails.append(d_users['l_d_clients'][client_num - 1].get_client_email())
            l_year.append('2019')
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_client_emails.append(d_users['l_d_clients'][client_num - 1].get_client_email())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
            admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                            client_team_member, l_client_name, l_year, l_client_bns, assert_result, l_client_emails)
            d_users['l_d_efile_auth_sendReminder_tasks'].append(admin_task_obj)

    def create_efiled_task_data(self, d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status):
        sub_menu_option = 'clientTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = 'Efile Auth'
        action = 'efiled'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = True

        #assigned Personal Task
        tab_name = 'personalTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_d_p_status[0][5]['Efiled'] += 1
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_efiled_tasks'].append(admin_task_obj)

        #assigned Business Task
        tab_name = 'businessTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name = []
            l_year = []
            l_client_bns = []
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
            admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                            client_team_member, l_client_name, l_year, l_client_bns, assert_result)
            d_users['l_d_efiled_tasks'].append(admin_task_obj)
            l_d_b_status[0][5]['Efiled'] += 2

    def test_data_insights_efiled_practice(self, d_users, l_d_b_status, l_d_p_status):
        obj_data_insights_practice = Test_data_insights_practice(
                                                                # l_d_status = [{'Initial': 0},{'Admin Review': 0}, {'Info Pending': 0}, {'Client Review': 0}, {'Efile Auth': 0}, {'Efiled': 0}, {'Closed': 2}],
                                                                # l_d_status = list().append(l_d_p_status[0]),
                                                                l_d_status = [{'Efiled':l_d_p_status[0][5]['Efiled']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Efiled':l_d_b_status[0][5]['Efiled']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)


    def create_closed_task_data(self, d_users, admin_num, num_bns, num_clients, l_d_b_status, l_d_p_status):
        sub_menu_option = 'closureTaskList'
        filter_year = 'All'
        tab_name = None
        filter_status = 'Efiled'
        action = 'close'
        client_team_member = None
        l_client_name = []
        l_year = []
        l_client_bns = None
        assert_result = True

        #assigned Personal Task
        tab_name = 'personalTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_d_p_status[0][6]['Closed'] += 1
        admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                        client_team_member, l_client_name, l_year, l_client_bns, assert_result)
        d_users['l_d_closed_tasks'].append(admin_task_obj)

        #assigned Business Task
        tab_name = 'businessTab'
        for client_num in range(1, num_clients + 1, 1):
            l_client_name = []
            l_year = []
            l_client_bns = []
            # filter_status = None,
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_name.append(d_users['l_d_clients'][client_num - 1].get_client_full_name())
            l_year.append('2019')
            l_client_bns = d_users['l_d_clients'][client_num - 1].get_c_bns_names()
            admin_task_obj = test_data_task(sub_menu_option, filter_year, tab_name, filter_status, action,
                                            client_team_member, l_client_name, l_year, l_client_bns, assert_result)
            d_users['l_d_closed_tasks'].append(admin_task_obj)
            l_d_b_status[0][6]['Closed'] += 2

    def test_data_insights_closed_practice(self, d_users, l_d_b_status, l_d_p_status):
        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Closed':l_d_p_status[0][6]['Closed']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Closed':l_d_b_status[0][6]['Closed']}],
                                                                filter_year = 'All',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)


    def create_data_messages(self, d_users):
        l_client_msgs = []
        l_team_msgs = []

        team_msg1 = ["Please complete this task on time",]
        team_msg2 = ['Sending for Manager Review']
        team_msg3 = ['Sending for CPA Review']
        client_msg1 = ['I have reviewed. Please e-file']
        client_msg2 = ['Sent for Efile authorization']
        client_msg3 = ['Authorized for efiling']
        #0
        msg_obj1 = test_data_msgs(client_msg = client_msg1)
        d_users['l_d_msgs'].append(msg_obj1)
        l_client_msgs.append(len(client_msg1))
        #1
        msg_obj2 = test_data_msgs(client_msg = client_msg2, second_clk_client=True)
        d_users['l_d_msgs'].append(msg_obj2)
        #2
        msg_obj3 = test_data_msgs(client_msg = client_msg3)
        d_users['l_d_msgs'].append(msg_obj3)
        l_client_msgs.append(len(client_msg3))
        #3
        team_msg_obj = test_data_msgs(team_msg = team_msg1, second_clk_team=True)
        d_users['l_d_msgs'].append(team_msg_obj)
        # l_team_msgs.append(len(team_msg1))
        #4
        team_msg_obj1 = test_data_msgs(team_msg = team_msg2)
        d_users['l_d_msgs'].append(team_msg_obj1)
        l_team_msgs.append(len(team_msg2))
        #5
        team_msg_obj2 = test_data_msgs(team_msg = team_msg3)
        d_users['l_d_msgs'].append(team_msg_obj2)
        l_team_msgs.append(len(team_msg3))
        return l_client_msgs, l_team_msgs

    def create_data_tickets(self, d_users, admin_num):
        # 0
        ticket_data_obj = Test_data_tickets(
                                    l_msg = ['ticket generated by CPA'],
                                    subject = 'check the business tab',
                                    l_l_files = [['sample (1).pdf', 'sample (2).pdf']],
                                    # tab_name = None,
                                    # ticket_num = None,
                                    )
        d_users['l_d_ticket'].append(ticket_data_obj)
     # super_admin reply to tickets
        # 1
        ticket_data_obj = Test_data_tickets(
                                    l_msg = ['Reply by super admin to ticket', 'Reply by super admin to ticket'],
                                    ticket_num = admin_num,
                                    # subject = None,
                                    # tab_name = None,
                                    l_l_files = [['sample (11).pdf', 'sample (12).pdf',],['sample (13).pdf', 'sample (14).pdf']]
                                    )
        d_users['l_d_ticket'].append(ticket_data_obj)
     # super_admin emp reply to tickets
        # 2
        ticket_data_obj = Test_data_tickets(
                                    l_msg = ['Reply by super admin emp to ticket', 'Reply by super admin emp to ticket'],
                                    ticket_num = admin_num,
                                    # subject = None,
                                    # tab_name = None,
                                    l_l_files = [['sample (3).pdf', 'sample (4).pdf',],['sample (5).pdf', 'sample (6).pdf']]
                                    )
        d_users['l_d_ticket'].append(ticket_data_obj)
    # CPA's reply
       # 3
        ticket_data_obj = Test_data_tickets(
                                   ticket_num = admin_num,
                                   l_msg = ["hi! i'm CPA, resolved ticket issue", "hi! i'm CPA, im closing ticket"],
                                   l_l_files = [['sample (7).pdf','sample (8).pdf',],['sample (9).pdf', 'sample (10).pdf']],
                                   # subject = None,
                                   # tab_name = None,
                                   )
        d_users['l_d_ticket'].append(ticket_data_obj)
    # CPA closeing ticket
       # 4
        ticket_data_obj = Test_data_tickets(
                                  # msg = None,
                                  # subject = None,
                                  # tab_name = None,
                                  # l_file = None,
                                  ticket_num = admin_num,
                                  )
        d_users['l_d_ticket'].append(ticket_data_obj)
     # super_admin checking closed tickets
        ticket_data_obj = Test_data_tickets(
                                    # msg = None,
                                    # subject = None,
                                    # tab_name = None,
                                    # l_file = None,
                                    ticket_num = admin_num
                                    )
        d_users['l_d_ticket'].append(ticket_data_obj)

    def create_profile_settings_data(self, d_users, mgr_num):

        client_name = d_users['l_d_clients'][mgr_num - 1].get_client_full_name()

    #unhecking chekboxes
        access_settings_obj1 = test_data_admin_profile(l_cl_ids_uncheck= ['Client-mgr',
                                    'Client-emp', 'Client-emp_direct', 'Business-mgr', 'Business-emp',
                                    'Business-emp_direct', 'PriceEstimate-mgr', 'PriceEstimate-emp', 'PriceEstimate-emp_direct',
                                    'Invoice-mgr', 'Invoice-emp', 'Invoice-emp_direct', 'InitialTaskList-mgr'])
        d_users['l_access_settings'].append(access_settings_obj1)

    #checking chekboxes
        access_settings_obj2 = test_data_admin_profile(l_cl_ids_check= ['Client-mgr',
                                    'Client-emp', 'Client-emp_direct', 'Business-mgr', 'Business-emp',
                                    'Business-emp_direct', 'PriceEstimate-mgr', 'PriceEstimate-emp', 'PriceEstimate-emp_direct',
                                    'Invoice-mgr', 'Invoice-emp', 'Invoice-emp_direct', 'InitialTaskList-mgr'])
        d_users['l_access_settings'].append(access_settings_obj2)
    #1
        emp_client_obj = test_data_doc_actions(client_name = client_name, tab_name= "PersonalTab", year = "2019")
        d_users['l_access_settings'].append(emp_client_obj)

# validating using id
    # validate obj1
        id_obj = test_data_admin_profile(l_validate_ids= ['unassignedTasks', 'clientTasks', 'closureTasks', 'extensionTasks'])
        d_users['l_verify_access_settings'].append(id_obj)
    # validate obj2
        id_obj1 = test_data_admin_profile(l_validate_ids= ['viewClientMessages', 'clientBusiness', 'clientPriceEst', 'clientInvoice'])
        d_users['l_verify_access_settings'].append(id_obj1)

    def test_data_insights_practice(self, d_users, l_emps_firstname,):
        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Info Pending': 0},],
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                l_d_status = [{'Info Pending':0},],
                                                                filter_year = 'All',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                # l_l_values = None,
                                                                # l_emp = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                # l_d_status = None,
                                                                filter_year = 'All',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'practiceInsights',
                                                                l_l_values = [[0, 0, 0, 0,],[0, 0, 0, 0,],[0, 0, 0, 0,]],
                                                                l_emp = l_emps_firstname,
                                                                l_status = ['Total', 'Assigned', 'In Progress', 'Mgr Review']
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

        obj_data_insights_practice = Test_data_insights_practice(
                                                                filter_year = 'All',
                                                                # l_d_status = None,
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'practiceInsights',
                                                                l_l_values = [[0, 0, 0, 0,],[0, 0, 0, 0,],[0, 0, 0, 0,]],
                                                                l_emp = l_emps_firstname,
                                                                l_status = ['Total', 'Assigned', 'In Progress', 'Mgr Review']
                                                                )
        d_users['l_d_insight_practice'].append(obj_data_insights_practice)

    def test_data_insights_client(self, d_users):
        obj_data_insights_client = Test_data_insights_client(
                                                                l_d_bns_type_or_service = [{'Sole-Prop':0},{'LP':0}, {'LLP':4}, {'LLC':0}, {'C-Corp':0}, {'S-Corp':0}, {'Non-Profit':0},{'Book-Keeping' : 4}, {'Payroll' : 4}, {'Sales Tax' : 4}, {'Tax Planning' : 4}],
                                                                filter_year = '2019',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'clientInsights',
                                                                # l_l_values = None,
                                                                # l_years = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_client'].append(obj_data_insights_client)

        obj_data_insights_client = Test_data_insights_client(
                                                                l_d_bns_type_or_service = [{'Sole-Prop':0},{'LP':0}, {'LLP':4}, {'LLC':0}, {'C-Corp':0}, {'S-Corp':0}, {'Non-Profit':0},{'Book-Keeping' : 4}, {'Payroll' : 4}, {'Sales Tax' : 4}, {'Tax Planning' : 4}],
                                                                filter_year = '2019',
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'clientInsights',
                                                                # l_l_values = None,
                                                                # l_years = None
                                                                # l_status = None
                                                                )
        d_users['l_d_insight_client'].append(obj_data_insights_client)

        obj_data_insights_client = Test_data_insights_client(
                                                                # l_d_status = None,
                                                                filter_year = '2019',
                                                                filter_category = 'Individual',
                                                                sub_menu_option = 'clientInsights',
                                                                l_l_values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]],
                                                                l_years = ['2017', '2018', '2019' ],
                                                                l_status = ['Lost Clients', 'Retained Clients', 'New Clients', 'Incomplete Clients']
                                                                )
        d_users['l_d_insight_client'].append(obj_data_insights_client)

        obj_data_insights_client = Test_data_insights_client(
                                                                filter_year = '2019',
                                                                # l_d_status = None,
                                                                filter_category = 'Business',
                                                                sub_menu_option = 'clientInsights',
                                                                l_l_values = [[0, 0, 0, 0,],[0, 0, 0, 0,],[0, 0, 4, 0,]],
                                                                l_years = ['2017', '2018', '2019' ],
                                                                l_status = ['Lost Clients', 'Retained Clients', 'New Clients', 'Incomplete Clients']
                                                                )
        d_users['l_d_insight_client'].append(obj_data_insights_client)

    def test_data_insight_growth(self, d_users, l_client_full_names, growth_insight_count, growth_insight_total_amount):
        individual_total_growth = growth_insight_total_amount-3
        individual_total_invoices = growth_insight_count - 2
        obj_data_insights_growth = Test_data_insights_growth(
                                                                l_d_invoice_breakdown = [{'Raised' : growth_insight_total_amount, 'invoice_count' : growth_insight_count },
                                                                                        {'Paid' : 0, 'invoice_count': 0},
                                                                                        {'Outstanding' : growth_insight_total_amount, 'invoice_count':growth_insight_count}],
                                                                filter_year = '2020',
                                                                sub_menu_option = 'growthInsights',
                                                                )
        d_users['l_d_insight_growth'].append(obj_data_insights_growth)

        obj_data_insights_growth = Test_data_insights_growth(
                                                                filter_year = '2020',
                                                                sub_menu_option = 'growthInsights',
                                                                l_l_d_invoice_year_and_values = [
                                                                                                  [{'2020':[individual_total_growth, 0, individual_total_growth,], 'rows':[individual_total_invoices, 0, individual_total_invoices,]},{'2018':[ 0, 0, 0,], "rows":[0,0,0]},{'2019':[ 0, 0, 0,], "rows":[0,0,0]},],
                                                                                                  [{'2020':[ individual_total_growth, 0, individual_total_growth,], 'rows':[individual_total_invoices, 0, individual_total_invoices,]},{'2018':[ 0, 0, 0,], "rows":[0,0,0]},{'2019':[ 0, 0, 0,], "rows":[0,0,0]},],
                                                                                                ],
                                                                l_client_name = l_client_full_names,
                                                                l_status = ['Raised', 'Paid', 'Outstanding']
                                                                )
        d_users['l_d_insight_growth'].append(obj_data_insights_growth)

    def create_notification_data(self, d_users, l_client_full_names, l_auto_todo_count):
        l_client_msgs_counts = []
        l_team_msgs_counts = []

        msg_res = self.create_data_messages(d_users)
        todo_res = self.create_todo_task_data(d_users)
        l_client_msgs_counts.extend([msg_res[0][0], msg_res[0][1]])
        l_team_msgs_counts.extend([msg_res[1][0], msg_res[1][1]])
        l_todo_tasks_count = todo_res
    # check notfification count
        # notification count of client
        notifi_obj1 = test_data_notifications(notification_type = "client_messages")
        d_users['l_notifi_count'].append(notifi_obj1)
        # notification count of team
        notifi_obj2 = test_data_notifications(notification_type = "team_messages")
        d_users['l_notifi_count'].append(notifi_obj2)
        # notification count of todo
        notifi_obj3 = test_data_notifications(notification_type = "todo_tasks")
        d_users['l_notifi_count'].append(notifi_obj3)
        # notification count of auto todo
        notifi_obj4 = test_data_notifications(notification_type = "auto_todo")
        d_users['l_notifi_count'].append(notifi_obj4)

    # emp client links
        emp_client_obj1 = test_data_doc_actions(client_name = l_client_full_names[0], tab_name= "PersonalTab", year = "2019")
        d_users['l_notifi_count'].append(emp_client_obj1)
        emp_client_obj2 = test_data_doc_actions(client_name = l_client_full_names[1], tab_name= "PersonalTab", year = "2019")
        d_users['l_notifi_count'].append(emp_client_obj2)

    # check notfification msg count
        # notification messges count of client
        notifi_msg_obj1 = test_data_notifications(notification_type = "client_messages", l_client_names = l_client_full_names,
                                                    l_client_msgs_counts= l_client_msgs_counts)
        d_users['l_notifi_msg_count'].append(notifi_msg_obj1)
        # notification messges count of team
        notifi_msg_obj2 = test_data_notifications(notification_type = "team_messages", l_team_names = [l_client_full_names[0]],
                                                    l_team_msgs_counts= l_team_msgs_counts)
        d_users['l_notifi_msg_count'].append(notifi_msg_obj2)
        notifi_msg_obj3 = test_data_notifications(notification_type = "team_messages", l_team_names = [l_client_full_names[1]],
                                                    l_team_msgs_counts= l_team_msgs_counts)
        d_users['l_notifi_msg_count'].append(notifi_msg_obj3)
        # notification messges count of todo
        notifi_msg_obj4 = test_data_notifications(notification_type = "todo_tasks", l_client_names = l_client_full_names,
                                                l_todo_tasks_count = l_todo_tasks_count)
        d_users['l_notifi_msg_count'].append(notifi_msg_obj4)
        # auto todo msg count
        notifi_msg_obj5 = test_data_notifications(notification_type = "auto_todo", l_client_names = l_client_full_names,
                                                l_auto_todo_count = [l_auto_todo_count[0] + l_auto_todo_count[1], l_auto_todo_count[2] + l_auto_todo_count[3]])
        d_users['l_notifi_msg_count'].append(notifi_msg_obj5)

    def create_reset_password_data(self, d_users):
        password = '123'
        retype_password = '1234'
        change_password_obj = Change_password(password = password, retype_password = retype_password)
        d_users['d_reset_password'] = change_password_obj

    def get_reset_password_data(self, admin_num):
        return self.l_d_users[admin_num-1]['d_reset_password']

    def get_admin_data(self, admin_num):
        return self.l_d_users[admin_num-1]['d_admin']

    def get_super_admin_data(self, admin_num):
        return self.l_d_users[admin_num-1]['d_super_admin']

    def get_super_admin_emp_data(self, admin_num):
        return self.l_d_users[admin_num-1]['d_super_admin_emp']

    def get_special_admin_data(self, admin_num):
        return self.l_d_users[admin_num-1]['d_special_admin']

    def get_special_mgr_data(self, admin_num):
        return self.l_d_users[admin_num-1]['d_special_mgr']

    def get_special_client_data(self, admin_num):
        return self.l_d_users[admin_num-1]['d_special_client']

    def get_all_client_data(self, admin_num, client_num = 0):
        try:
            client_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_clients']
        else:
            if client_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_clients']
            else:
                return self.l_d_users[admin_num - 1]['l_d_clients'][client_num - 1]

    def get_auto_todo_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_auto_todo']

    def get_all_client_update_profile_data(self, admin_num, client_num = 0):
        try:
            client_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_update_client_profile']
        else:
            if client_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_update_client_profile']
            else:
                return self.l_d_users[admin_num - 1]['l_d_update_client_profile'][client_num - 1]

# price calculation
    def get_price_cal_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['d_price_cal']
    def get_price_est_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_d_price_est']

# invoice e2e
    def get_add_invoice_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_invoice']
    def get_verify_invoice_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_invoice_verify']

# todo task
    def get_todo_task_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_todo_tasks']

# notifications
    def get_notifi_count_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_notifi_count']
    def get_notifi_msg_count_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_notifi_msg_count']

    def get_all_rcp_data(self, admin_num, rcp_num = 0):
        try:
            rcp_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_rcp']
        else:
            if rcp_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_rcp']
            else:
                return self.l_d_users[admin_num - 1]['l_d_rcp'][rcp_num - 1]

    def get_all_special_rcp_data(self, admin_num, rcp_num = 0):
        try:
            rcp_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_special_rcp']
        else:
            if rcp_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_special_rcp']
            else:
                return self.l_d_users[admin_num - 1]['l_d_special_rcp'][rcp_num - 1]

    def get_all_mgrs_data(self, admin_num, mgr_num = 0):
        try:
            mgr_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_mgrs']
        else:
            if mgr_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_mgrs']
            else:
                return self.l_d_users[admin_num - 1]['l_d_mgrs'][mgr_num - 1]

    def get_all_emps_data(self, admin_num, mgr_num = 0, emp_num = 0):
        try:
            emp_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_emps']
        else:
            if emp_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_emps']
            else:
                return self.l_d_users[admin_num - 1]['l_d_emps'][2*(mgr_num - 1) + emp_num - 1]

    def get_all_doc_data(self, admin_num, doc_num = 0):
        try:
            doc_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_doc']
        else:
            if doc_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_doc']
            else:
                return self.l_d_users[admin_num - 1]['l_d_doc'][doc_num - 1]

    def get_all_msgs_data(self, admin_num, msg_num = 0):
        try:
            msg_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_msgs']
        else:
            if msg_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_msgs']
            else:
                return self.l_d_users[admin_num - 1]['l_d_msgs'][msg_num - 1]

    def get_all_unassigned_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_unassigned_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_unassigned_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_unassigned_tasks'][task_num - 1]

    def get_all_assigned_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_assigned_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_assigned_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_assigned_tasks'][task_num - 1]

    def get_all_due_date_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_due_date_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_due_date_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_due_date_tasks'][task_num - 1]

    def get_all_mgr_review_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_mgr_review_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_mgr_review_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_mgr_review_tasks'][task_num - 1]

    def get_all_admin_review_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_admin_review_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_admin_review_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_admin_review_tasks'][task_num - 1]

    def get_all_client_review_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_client_review_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_client_review_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_client_review_tasks'][task_num - 1]

    def get_all_efile_auth_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_efile_auth_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_efile_auth_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_efile_auth_tasks'][task_num - 1]

    def get_all_efile_auth_sendReminder_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_efile_auth_sendReminder_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_efile_auth_sendReminder_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_efile_auth_sendReminder_tasks'][task_num - 1]

    def get_all_efiled_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_efiled_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_efiled_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_efiled_tasks'][task_num - 1]

    def get_all_closed_tasks_data(self, admin_num, task_num = 0):
        try:
            task_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_closed_tasks']
        else:
            if task_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_closed_tasks']
            else:
                return self.l_d_users[admin_num - 1]['l_d_closed_tasks'][task_num - 1]

    def get_all_client_delete_data(self, admin_num, client_num = 0):
        try:
            client_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_clients_delete']
        else:
            if client_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_clients_delete']
            else:
                return self.l_d_users[admin_num - 1]['l_d_clients_delete'][client_num - 1]



    def get_all_mgrs_delete_data(self, admin_num, mgr_num = 0):
        try:
            mgr_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_mgrs_delete']
        else:
            if mgr_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_mgrs_delete']
            else:
                return self.l_d_users[admin_num - 1]['l_d_mgrs_delete'][mgr_num - 1]

    def get_all_admin_team_action_data(self, admin_num, action_num = 0):
        try:
            action_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_team_actions']
        else:
            if action_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_team_actions']
            else:
                return self.l_d_users[admin_num - 1]['l_d_team_actions'][action_num - 1]

    def get_all_admin_client_action_data(self, admin_num, action_num = 0):
        try:
            action_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_client_actions']
        else:
            if action_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_client_actions']
            else:
                return self.l_d_users[admin_num - 1]['l_d_client_actions'][action_num - 1]

    def get_all_admin_ticket_action_data(self, admin_num, action_num = 0):
        try:
            action_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_ticket']
        else:
            if action_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_ticket']
            else:
                return self.l_d_users[admin_num - 1]['l_d_ticket'][action_num - 1]

    def get_all_admin_appointment_test_data(self, admin_num, action_num = 0):
        try:
            action_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_appointments']
        else:
            if action_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_appointments']
            else:
                return self.l_d_users[admin_num - 1]['l_d_appointments'][action_num - 1]

    def get_all_admin_insights_practice_data(self, admin_num, action_num = 0):
        try:
            action_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_insight_practice']
        else:
            if action_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_insight_practice']
            else:
                return self.l_d_users[admin_num - 1]['l_d_insight_practice'][action_num - 1]

    def get_all_admin_insights_client_data(self, admin_num, action_num = 0):
        try:
            action_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_insight_client']
        else:
            if action_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_insight_client']
            else:
                return self.l_d_users[admin_num - 1]['l_d_insight_client'][action_num - 1]

    def get_all_admin_insights_growth_data(self, admin_num, action_num = 0):
        try:
            action_num
        except KeyError:
            return self.l_d_users[admin_num - 1]['l_d_insight_growth']
        else:
            if action_num == 0:
                return self.l_d_users[admin_num - 1]['l_d_insight_growth']
            else:
                return self.l_d_users[admin_num - 1]['l_d_insight_growth'][action_num - 1]

# profile settings e2e
    def get_access_settings_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_access_settings']
    def get_verify_access_settings_data(self, admin_num):
        return self.l_d_users[admin_num - 1]['l_verify_access_settings']
