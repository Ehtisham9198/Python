
# to know about plateform(laptop)
import platform
x=platform.system()
print(x)
print(dir(platform))

import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())

# DOB ->Age in YYYY-MM-DD formate

import datetime

def calculate_age(birth_date):
    current_date = datetime.date.today()
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    
    years = age
    months = 0
    days = 0
    
    if current_date.month < birth_date.month:
        years -= 1
        months = 12 - (birth_date.month - current_date.month)
    elif current_date.month == birth_date.month:
        if current_date.day < birth_date.day:
            years -= 1
            months = 11
            days = (30 - birth_date.day) + current_date.day
    else:
        months = current_date.month - birth_date.month
    
    age_in_YYYY_MM_DD_format = f"{years:04d}-{months:02d}-{days:02d}"
    
    return age_in_YYYY_MM_DD_format



DOB = datetime.date(1990, 5, 15) 
age_in_YYYY_MM_DD_format = calculate_age(DOB)
print("Age in YYYY-MM-DD format:", age_in_YYYY_MM_DD_format)