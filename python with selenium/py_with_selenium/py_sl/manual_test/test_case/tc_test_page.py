from py_sl.manual_test.base import base_test_case
from py_sl.manual_test.common_func import common_utils
from py_sl.manual_test.pages.test_page import test_page_func
import pytest

@pytest.mark.test_page
class Test_page(base_test_case):
    def test_1_signin(self):
        super(Test_page, self).get_driver()
        params = dict()
        response = dict()
        params['user_name'] = "sarah.walker@cpa.com"
        params['password'] = "Cpasage@123"
        obj_signin = common_utils(self.driver)
        obj_signin.signin(params, response)

    def test_2_nav_to_client_actions(self):
        super(Test_page, self).get_driver()
        params = dict()
        response = dict()
        params['driver'] = self.driver
        test_page_func(params, response)

    def test_3_driver_quit(self):
        super(Test_page, self).quit()








