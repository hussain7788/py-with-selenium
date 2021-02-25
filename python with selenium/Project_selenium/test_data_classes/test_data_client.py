d_config = {"path":'/home/gangah/Documents/'}
class test_data_client():
    first_name = None
    last_name = None
    email =  None
    phone =  None
    password =  None
    l_bns = None
    l_file_dtls = None

    def __init__(self, first_name=None, last_name=None, email=None, phone=None, password=None, l_bns=None,
                                    l_file_dtls=None,):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        self.l_bns = l_bns
        self.l_file_dtls = l_file_dtls

    def get_data(self):
        return_dict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'phone': self.phone,
                'password': self.password,
               }

        return_dict['l_d_bns'] = []
        for bns in self.l_bns:
            return_dict['l_d_bns'].append(bns.get_data())

        return_dict['l_d_upload'] = []
        for file_dtl in self.l_file_dtls:
            return_dict['l_d_upload'].append(file_dtl.get_data())

        return return_dict

    def get_client_data(self):
        return_dict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'phone': self.phone,
                'password': self.password,
               }
        return return_dict

    def get_client_link(self):
        return {'client_link' : self.email, 'tab_name' : "activeTab"}

    def get_client_full_name(self):
        return str(self.first_name + " " + self.last_name)

    def get_client_email(self):
        return str(self.email)

    def get_c_bns_data(self):
        return_list = []
        for bns in self.l_bns:
            return_list.append(bns.get_data())
        return return_list

    def get_c_bns_names(self):
        return_list = []
        for bns in self.l_bns:
            return_list.append(bns.get_bns_name())
        return return_list

    def get_c_files_data(self):
        return_list = []
        for file_dtl in self.l_file_dtls:
            return_list.append(file_dtl)
        return return_list

    def get_data_signin(self):
        return {
                'user_name': self.email,
                'password': self.password
               }

class test_data_business():

    def __init__(self, bns_name=None, bns_type=None, bns_inc_state=None, bns_inc_date=None, bk_frequency=None,  pr_frequency=None,
                                                st_frequency=None, tp_checkbox=None, tp_frequency=None):
        self.bns_name = bns_name
        self.bns_type = bns_type
        self.bns_inc_state = bns_inc_state
        self.bns_inc_date = bns_inc_date
        self.bk_frequency = bk_frequency
        self.pr_frequency = pr_frequency
        self.st_frequency = st_frequency
        self.tp_checkbox = tp_checkbox
        self.tp_frequency = tp_frequency

    def get_data(self):
        return_dict= {
                        'bns_name': self.bns_name,
                        'bns_type': self.bns_type,
                        'bns_inc_state': self.bns_inc_state,
                        'bns_inc_date': self.bns_inc_date,
                        'pr_checkbox': True,
                        'pr_frequency': self.pr_frequency,
                        'bk_checkbox': True,
                        'bk_frequency': self.bk_frequency,
                        'st_checkbox': True,
                        'st_frequency': self.st_frequency,
                        'tp_checkbox': self.tp_checkbox,
                        'tp_frequency': self.tp_frequency,
                    }
        if self.pr_frequency == "None":
            return_dict['pr_checkbox'] = False
        if self.bk_frequency == "None":
            return_dict['bk_checkbox'] = False
        if self.st_frequency == "None":
            return_dict['st_checkbox'] = False
        return return_dict

    def get_bns_name(self):
        return self.bns_name

    def get_bns_data(self):
        return_list = []
        return_list.append(test_data_business.get_data(self))
        return return_list

class test_data_upload_files():

    def __init__(self, tab_name=None, sub_tab=None, client_login_access=None, tax_year=None,
                            document_source=None, bns_name=None, l_files=None,):
        self.tab_name = tab_name
        self.sub_tab = sub_tab
        self.client_login_access = client_login_access
        self.tax_year = tax_year
        self.bns_name = bns_name
        self.document_source = document_source
        self.l_files = l_files

    def get_data(self):
        return_dict = {
                        'tab_name': self.tab_name,
                        'sub_tab': self.sub_tab,
                        'client_login_access': self.client_login_access,
                        'tax_year': self.tax_year,
                        'bns_name': self.bns_name,
                        'document_source': self.document_source,

                      }
        return_dict['file_details'] = []
        for file in self.l_files:
            return_dict['file_details'].append(file.get_data())
        return return_dict

class test_data_file():
    file_name = None
    file_type = None

    def __init__(self, file_name, file_type):
        self.file_name = file_name
        self.file_type = file_type

    def get_data(self):
        return {
                'file_name': self.file_name,
                'full_file_name': str(d_config['path'] + self.file_name),
                'file_type': self.file_type
               }
class test_data_msgs():
    def __init__(self, client_msg=None,  team_msg=None, send_msg_access=True):
        self.client_msg = client_msg
        self.team_msg = team_msg
        self.send_msg_access = send_msg_access

    def get_data(self):
        return {
                'client_msg': self.client_msg,
                'team_msg': self.team_msg,
                'send_msg_access' : self.send_msg_access,
               }
