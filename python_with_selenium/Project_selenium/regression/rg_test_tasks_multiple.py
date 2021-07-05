from pm.test.regression.rg_test_data_gen import *
from pm.test.regression.rg_task_transitions import *
import pdb

@pytest.mark.test_all
@pytest.mark.test_e2e_tasks
# @pytest.mark.parametrize("name")
class Test_tasks(base_test_case):
    def test_1_e2e_usecase(self, offset):
        super(Test_tasks, self).get_driver()
        tc_pre_process()
        params = {}
        response = {}
        params['num_admins'] = 1 # number of admins
        params['num_clients'] = 2 # per admin
        params['num_bns'] = 2 # per client
        params['num_bns_files'] = 2 # per business
        params['num_per_files'] = 3 # per client (personal files)
        params['num_rcp'] = 1 # per admin
        params['num_mgrs'] = 2 # per admin
        params['num_emps'] = 2 # per mgr
        params['num_invoices'] = 2 # per client
        params['ticket_test'] = 'no' # to run the ticket test make sure that database is cleard and offset to 1.
        params['appointment_test'] = 'no'
        params['client_team_action_test'] = 'no'
        params['offset'] = int(offset)
        params['path'] = '/home/gangah/Documents/'
        params['d_price_cal'] =  {'Tax Return': 30, 'W-2': 20, '1099-B': 1, '1099-INT': 2, '1099-DIV': 3,
                                  '1099-MISC': 4, '1099-R': 5, '1098': 6, 'Property Tax': 7, 'Cash Donation': 8,
                                  'Non-cash Donation': 9, 'P&L': 10, 'Bank Statement': 11}

        obj = test_data_gen(params, response)
        obj.set_base_data()

        for admin_num in range(1, params['num_admins'] + 1, 1):
            execute_task_transitions(self.driver, obj, admin_num)

    def test_2_destroy_instance(self, offset):
        super(Test_tasks, self).destroy_driver()
        tc_post_process()
