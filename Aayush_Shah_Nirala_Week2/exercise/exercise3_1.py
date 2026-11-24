# 3.1 Write a Python program that calculates an employee's pay based on their regular
# hours and overtime hours worked in a week. The standard workweek is 40 hours, and
# any hours worked beyond that are considered overtime. An employee must receive
# overtime pay for hours worked over 40 in a work week at a rate of 1.5 times regular
# rates of pay. The hourly wage is £22.

# Input the employee's name and number of hours worked in a week.
# Calculate the total pay for regular hours.
# If the employee worked more than 40 hours, calculate the overtime pay.
# Calculate the total pay in a week.
# Print the employee's name, regular pay, overtime pay and the total pay.

rate = 22

emoployee_name = input("Enter employee name: ")
hours = float(input("Enter total hours worked in a week: "))

if hours <= 40:
    regular_pay = hours * rate
    overtime_pay = 0
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    
total_pay = regular_pay + overtime_pay

print("Employee name: ", emoployee_name)
print("Regular Pay: ", regular_pay)
print("Overtime Pay: ", overtime_pay)
print("Total Pay: ", total_pay)
    
    