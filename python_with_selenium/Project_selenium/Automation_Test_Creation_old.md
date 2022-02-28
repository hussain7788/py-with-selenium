ECHO is on.

web_page --> first understand web_page requirement.

locators --> -In selenium to perform action on any object of HTML we need to select it using unique Id.
-Locators are nothing but id's of HTML element.
-we define locators in Locators directory by creating static variables of class.
ex. # Locators for Adding Clients
class lc_admin_add_client():
add_client = "addClientBtn"
first_name = "firstName"
last_name = "lastName"
email = "email"
phone = "phone"

$ we have common_functions in utils directory for new registration, sign-in, navigation and table validation. (here we get web-driver in URL)

$ tc_base.py is in test_cases directory which is used to decide(headless) mode of the driver.

Notes: 1. do not send ids as a parameter in test*case 2. do the validation coding in tcf(test_case_func). 3. naming convention --> "pg*" prefix for page object.
--> "tcf\_" prefix for test case functions.
--> give such name which tells about functionality of code.

page_obj --> -create page object using sl_functions.py module functions.
----> sl_functions.py all functions are nothing but selenium. this module is created to separate selenium from page_obj so if there is any change in selenium, we just need to change at sl_functions module.
-Use locators to locate HTML element using selenium code.
-we should write page_obj classes and methods in such way that we can call them single or multiple times to match the webpage behaviour .

             ex.:
                 from pm.test.locators.lc_admin import *
                 from pm.test.locators.lc_common import *
                 from pm.test.locators.lc_super_admin import *
                 from pm.test.utils.common_functions import *
                 from pm.test.selenium_utility.sl_functions import *

                 class pg_admin_add_client(navigation): # navigation class is inherited. navigation class is present in cpa_pm/pm/test/utils folder in common_functions module.
                     def __init__(self, driver):
                         self.driver = driver
                         super(pg_admin_add_client, self).__init__(driver) # Here we are passing driver to the navigation class constructor of common_functions module

                     def navigate_add_client(self, params, response):
                         driver = self.driver
                         params = dict()
                         response = dict()
                         params['menu_option'] = lc_admin_menu.client_actions
                         super(pg_admin_add_client, self).menu_navigation(params, response)
                                            # Here we are passing parameters to the menu_navigation method of common_functions module.
                       # sl_time_sleep(1)

                     def add_client(self, params, response):
                         driver = self.driver
                         sl_button_click(driver, lc_admin_add_client.add_client)
                         sl_send_keys(driver, lc_admin_add_client.first_name, params['first_name'])
                         sl_send_keys(driver, lc_admin_add_client.last_name, params['last_name'])
                         sl_send_keys(driver, lc_admin_add_client.email, params['email'])
                         sl_send_keys(driver, lc_admin_add_client.phone, params['phone'])
                         sl_button_click(driver, lc_all_common.save_btn)
                         sl_refresh(driver)

test_case_functions --> -Test case functions work as brain in our tests.
-We achive webpage behaviour in test case functions.
-Here we call page obj classes and their methods.
-we create tcf_methods as per functionality.
ex.
class tcf_admin_add():
def admin_add_client(self, params, response):
if len(params['l_client']) == 0:
response['result'] = True
return True
driver = params['driver']
obj_admin_add_client = pg_admin_add_client(driver)
obj_admin_add_client.navigate_add_client({}, response)
#sl_time_sleep()
########################## # These two lists l_l_primary_values and l_l_misc_values are needed for table_validation
l_l_primary_values = list()
l_l_misc_values = list()
########################## # Add all the clients that have been passed to the function
for client in params['l_client']:
obj_admin_add_client.add_client(client, response)
l_l_primary_values.append([client['email']])
l_l_misc_values.append([client['first_name'], client['last_name'], client['phone']])
############### # Prepare the data to verify that the records have been added successfully
params['tab_name'] = "activeTab"
params['misc'] = True
params['table_id'] = "activeTable"
params['l_primary_col'] = ["Email"]
params['l_l_primary_values'] = l_l_primary_values
params['l_misc_col'] = ["First Name", "Last Name", "Phone Number"]
params['l_l_misc_values'] = l_l_misc_values

                                obj_table_validation = table_validation.get_instance()
                                ret = obj_table_validation.table_search(params, response)
                                print("Result: " + str(response['result']))
                                print("Result List: " + str(response['l_result_per_primary_value']))
                                return ret

data classes --> -why data classes?
-> for data_obj creation
-> we use this data classes to generate data objects to run transactions based test cases.
-> we pass this data objects to test_transaction function

            ex.
            #### data class for client ####
            ##### cpa_pm/pm/test/test_data/test_data_class ####
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

              #####  data object creation using data classes ######
                d_users = {
                    'l_d_admin': [],
                    'l_emp_info' : [],
                    'l_d_client' : [],
                }

                def data_admin():
                # data_object created for admin
                    admin_data_obj = test_data_admin(
                                            first_name = "Sarah",
                                            last_name = "Walker",
                                            email = "sarah.walker@cpa.com",
                                            company_name = "yours_efficiently",
                                            phone = '123456789',
                                            password = "123",
                                        )
                  # obj added to the list of l_d_admin
                    d_users['l_d_admin'].append(admin_data_obj)

                def data_client():

                    for i in range(1, 4, 1):
                        first_name = str("f" + str(i))
                        last_name = str("l" + str(i))
                        email = str(first_name + "." + last_name + "client.com")
                        phone = "123-456-7890"

                      # same way data is created using client data class and appended them to l_emp_info

                        client_user_obj = test_data_client(first_name, last_name, email, phone, l_bns = None, l_file_dtls= None, password = "123")
                        d_users['l_d_client'].append(client_user_obj)

                def data_init():
                    data_admin()
                    data_client()

once you done with this, you can move towards creating data classes and writing end to end test cases using transactions.

transactions --> -transactions nothing but a collection of tcf with conditional flasgs. That conditional flags nothing but key(string).
-To use tcf mentioned in transactions we need to pass key and object of data to test_transaction object.

test*cases --> -we are using pytest framework to run automated test cases.(always write "test*" prefix to every method name)
-Don't forget to give unique pytest marker name.
-We write test_cases here which will run automatically.
-Here we test one by one functionality of web page.

               l_transactions = []

               @pytest.mark.test_all
               @pytest.mark.test_admin
               class Test_admin_add(base_test_case):
                   def test_1_signin(self):
                       data_init()                              # here we are calling function for data creation.
                       super(Test_admin_add, self).get_driver() # getting web driver
                       driver = self.driver
                   # 0
                   # CPA Signin
                   # creating test_transactions objects and appending them to l_transactions
                       obj_transaction = test_transaction('pm_key_signin', d_users['l_d_admin'][0])
                       l_transactions.append(obj_transaction)

                       obj_transaction = test_transaction('pm_key_add_client', d_users['l_d_client'])
                       l_transactions.append(obj_transaction)

                       execute_transactions(l_transactions, driver)

                   def test_2_destroy_instance(self):
                       super(Test_admin_add, self).destroy_driver()
                       tc_post_process()

test.py --> import test_case file in test.py

use data_classes and test_transaction for scaling test(regression test)
