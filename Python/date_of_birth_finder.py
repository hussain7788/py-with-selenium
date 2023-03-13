from datetime import date

def find_date_of_birth():
    date_of_birth = input("Enter data of birth in the format of \'Y-M-D\' :", )

    l_dates = date_of_birth.split('-')
    year = int(l_dates[0])
    month = int(l_dates[1])
    day = int(l_dates[2])

    org_date = date(year, month, day)
    date_now = date.today()

    total_months = (date_now - org_date)/30
    total_years = total_months/12
    return (f"Months :{total_months.days} \n \r Years: {total_years.days}")

print(find_date_of_birth())


############### Find years After 2 Years from today ###############
def second_method():
    from datetime import datetime, timedelta

    present_datetime = datetime.now()

    d1 = datetime(1996, 12, 13)

    after_2_yrs = present_datetime + timedelta(days=730)

    print(after_2_yrs)
    age = (present_datetime-d1)/365.2425
    print(age.days, "years")

print(second_method())


################### using dateutil relative delta method #####################
from dateutil.relativedelta import relativedelta
from datetime import date

def calculate_age(birth_date):
	today = date.today()
	age = relativedelta(today, birth_date)
	return age.years

# Test the function
birth_date = date(1997, 2, 3)
age = calculate_age(birth_date)
# print(f"Age in years: {age}")




