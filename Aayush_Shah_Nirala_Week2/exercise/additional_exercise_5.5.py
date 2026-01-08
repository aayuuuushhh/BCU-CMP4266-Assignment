# 5.5 Write a program to determine whether an employee is owed any overtime.
# You should ask the user how many hours the employee worked in a specific week,
# as well as the hourly wage for this employee. If the employee worked more than 40 hours, 
# you should print a message which says the employee is due some additional pay, as well as the amount due.
# The additional amount owed is 20% of the employee’s hourly wage for each hour worked over the 40 hours.

h = float(input("Enter hours they worked this week:"))
w = float(input("Enter hourly wage:"))
if h >40:
    overtime_hour = h -40
    overtime_pay = overtime_hour * w * 0.20
    print("Employee is due additional pay.")
    print(f"Overtime hours:{overtime_hour}")
    print(f"Additional pay:{overtime_pay}")
else:
    print("No overtime pay is due.")