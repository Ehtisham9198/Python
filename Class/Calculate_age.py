import datetime
def calculate_age(birth_date):
    current_date = datetime.date.today()
    age = current_date.year - birth_date.year
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
    
    actual_age = f"{years}-{months}-{days}"
    
    return actual_age



DOB = datetime.date(1990, 5, 15) 
age = calculate_age(DOB)
print("Age:", age)


# {Timestamp in one timezone}->another time zone
# Calculate total business hours between two date time obj considering a specific set of working hour and excluding weekends and holidays
# 