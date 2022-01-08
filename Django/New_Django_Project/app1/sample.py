import datetime
list1 = [{'id': 1, 'ut_admin_id': 2, 'ut_user_id': 1, 'ut_user_name': 'Percy Jackson', 'ut_user_email': 'percy.jackson@client.com', 'ut_bns_id': 0, 'ut_bns_name': '', 'ut_cat_id': 1, 'ut_cat_name': 'Personal', 'ut_year': 2016, 'ut_current_status': 1, 'ut_current_status_name': 'Initial', 'int_prev_status': 1, 'int_prev_status_name': 'Initial', 'ut_status_updated_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 139636), 'ut_last_uploaded_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 151546), 'ut_assign_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 139687, ), 'ut_emp_assigned': 0, 'ut_emp_assigned_name': 'Sarah Walker', 'ut_mgr_assigned_name': 'Sarah Walker', 'ut_mgr_assigned': 0, 'int_prev_emp': 0, 'int_prev_mgr': 0, 'ut_due_date': datetime.datetime(2021, 6, 25, 13, 47, 2, 440000, ), 'ut_mgr_assigned_date': None, 'ut_emp_assigned_date': None, 'ut_estimated_price': 0, 'ut_price_adjustments': 0, 'flag': 0, 'flag2': 0}, {'id': 2, 'ut_admin_id': 2, 'ut_user_id': 1, 'ut_user_name': 'Percy Jackson', 'ut_user_email': 'percy.jackson@client.com', 'ut_bns_id': 0, 'ut_bns_name': '', 'ut_cat_id': 1, 'ut_cat_name': 'Personal', 'ut_year': 2017, 'ut_current_status': 2, 'ut_current_status_name': 'Assigned', 'int_prev_status': 2, 'int_prev_status_name': 'Assigned', 'ut_status_updated_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 193322, ), 'ut_last_uploaded_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 182691, ), 'ut_assign_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 174444, ), 'ut_emp_assigned': 6, 'ut_emp_assigned_name': 'Kyrie Irving', 'ut_mgr_assigned_name': 'Morgan Grimes', 'ut_mgr_assigned': 4, 'int_prev_emp': 6, 'int_prev_mgr': 4, 'ut_due_date': datetime.datetime(2021, 6, 17, 12, 43, 12, 182776, ), 'ut_mgr_assigned_date': datetime.datetime(2021, 6, 10, 12, 43, 12, 182797, ), 'ut_emp_assigned_date': datetime.datetime(2021, 6, 10, 12, 43, 12, 182795, ), 'ut_estimated_price': 0, 'ut_price_adjustments': 0, 'flag': 0, 'flag2': 0}, {
    'id': 3, 'ut_admin_id': 2, 'ut_user_id': 1, 'ut_user_name': 'Percy Jackson', 'ut_user_email': 'percy.jackson@client.com', 'ut_bns_id': 0, 'ut_bns_name': '', 'ut_cat_id': 1, 'ut_cat_name': 'Personal', 'ut_year': 2018, 'ut_current_status': 3, 'ut_current_status_name': 'In Progress', 'int_prev_status': 3, 'int_prev_status_name': 'In Progress', 'ut_status_updated_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 311767, ), 'ut_last_uploaded_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 269972, ), 'ut_assign_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 259834, ), 'ut_emp_assigned': 6, 'ut_emp_assigned_name': 'Kyrie Irving', 'ut_mgr_assigned_name': 'Morgan Grimes', 'ut_mgr_assigned': 4, 'int_prev_emp': 6, 'int_prev_mgr': 4, 'ut_due_date': datetime.datetime(2021, 6, 17, 12, 43, 12, 270061, ), 'ut_mgr_assigned_date': datetime.datetime(2021, 6, 10, 12, 43, 12, 270083, ), 'ut_emp_assigned_date': datetime.datetime(2021, 6, 10, 12, 43, 12, 270081, ), 'ut_estimated_price': 0, 'ut_price_adjustments': 0, 'flag': 0, 'flag2': 0}, {'id': 4, 'ut_admin_id': 2, 'ut_user_id': 1, 'ut_user_name': 'Percy Jackson', 'ut_user_email': 'percy.jackson@client.com', 'ut_bns_id': 0, 'ut_bns_name': '', 'ut_cat_id': 1, 'ut_cat_name': 'Personal', 'ut_year': 2019, 'ut_current_status': 4, 'ut_current_status_name': 'Mgr Review', 'int_prev_status': 4, 'int_prev_status_name': 'Mgr Review', 'ut_status_updated_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 520761, ), 'ut_last_uploaded_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 486392, ), 'ut_assign_time': datetime.datetime(2021, 6, 10, 12, 43, 12, 474269, ), 'ut_emp_assigned': 6, 'ut_emp_assigned_name': 'Kyrie Irving', 'ut_mgr_assigned_name': 'Morgan Grimes', 'ut_mgr_assigned': 4, 'int_prev_emp': 6, 'int_prev_mgr': 4, 'ut_due_date': datetime.datetime(2021, 6, 17, 12, 43, 12, 486495, ), 'ut_mgr_assigned_date': datetime.datetime(2021, 6, 10, 12, 43, 12, 486526, ), 'ut_emp_assigned_date': datetime.datetime(2021, 6, 10, 12, 43, 12, 486522), 'ut_estimated_price': 0, 'ut_price_adjustments': 0, 'flag': 0, 'flag2': 0}]
# print("list:::::", list1)
for i in list1:
    print(i['ut_estimated_price'])


class CommonClass(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Teacher(CommonClass):
    salary = models.FloatField()
