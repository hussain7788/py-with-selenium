from py_sl.manual_test.base import base_test_case
from py_sl.manual_test.common_func import navigation,common_utils

from py_sl.manual_test.pages.test_page import test_page_func

class execute_test_page(base_test_case):
    def test1_page(self):
        super(execute_test_page, self).get_driver()
        self.driver = driver
        params = dict()
        response = dict()
        params['user_name'] = "sarah.walker@cpa.com"
        params['password'] = "Cpasage@123"
        obj_signin = common_utils(self.driver)
        obj_signin.signin(params, response)
    
    def test2_nav_to_client_actions(self):
        super(execute_test_page, self).get_driver()
        params = dict()
        response = dict()
        params['driver'] = self.driver
        test_page_func(params, response)
    
    def driver_quit(self):
        super(execute_test_page, self).quit()


obj_test = execute_test_page()
obj_test.test1_page()
obj_test.test2_nav_to_client_actions()
obj_test.driver_quit()




    


