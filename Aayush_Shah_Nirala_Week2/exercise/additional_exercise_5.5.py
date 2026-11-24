# 5.5 Write a Python program to calculate the price of a theater ticket. Your program should
# prompt the user for their age. The standard ticket price is £10. Children (aged 12 and
# under) and seniors (aged 65 and older) receive a 20% discounted ticket. Your
# program should calculate and display the ticket price based on the age entered.

price = 10

age = int(input("Enter your age: "))

if age <=12 or age >= 65:
    discount_price = price * 0.8
else:
    discount_price = price
    
print("Ticket price: ", discount_price)