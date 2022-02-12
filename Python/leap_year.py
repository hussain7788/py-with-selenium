
year = int(input("Enter year to be checked:"))
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year")


year = 2020

if year % 4== 0 and year %100 != 0 or year % 400 == 0:
    print(year, "leap")
else:
    print(year, "not leap") 