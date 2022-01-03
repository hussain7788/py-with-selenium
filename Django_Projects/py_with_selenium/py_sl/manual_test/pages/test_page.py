from py_sl.manual_test.common_func import navigation

def test_page_func(params, response):
    obj = test_page(params['driver'])
    obj.nav_to_client_actions(params, response)

class test_page(navigation):
    def __init__(self, driver):
        self.driver = driver
        super(test_page, self).__init__(driver)

    def nav_to_client_actions(self, params, response):
        driver = self.driver
        params['main_menu'] = "clientActions"
        super(test_page, self).manu_nav(params, response)
