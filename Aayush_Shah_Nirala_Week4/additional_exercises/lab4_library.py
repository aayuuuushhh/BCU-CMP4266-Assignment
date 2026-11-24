def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
def get_days_of_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31 
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap(year):
            return 29 
        else:
            return 28
    else:
        return "Invalid month"