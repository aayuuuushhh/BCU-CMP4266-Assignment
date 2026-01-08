import lab4_library
def days_in_month(month, year):
    days = lab4_library.get_days_of_month(month, year)
    if days is None:
        print(f"Error: invalid month: {month}")
    else:
        print(f"In {year}, month {month} has {days} days.")

days_in_month(1, 2021)
days_in_month(2, 2020)
days_in_month(13, 2000)