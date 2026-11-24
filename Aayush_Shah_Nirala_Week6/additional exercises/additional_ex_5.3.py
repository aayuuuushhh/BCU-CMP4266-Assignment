# 5.3 Create in Python the program containing a function, called report, which creates a
# short report of the quantities of spare parts sold in three different stores (located in London, Birmingham
# and Nottingham). The function:

# . receives three mandatory parameters (q1, q2 and q3) containing the quantities sold,
# respectively, in London, Birmingham and Nottingham.
# . receives three optional parameters containing the price of the spare parts: € 60 for spare parts
# sold in London, € 57 for those sold in Birmingham and € 59 for those sold in Nottingham.
# . calculates the revenue of each store, the average quantity sold and the average revenue.
# . create a report similar to the example shown below, showing two decimal digits for revenues
# and one decimal digit for the average quantity sold.

def report(q1, q2, q3, p1 = 60, p2 = 57, p3 = 59):
    revenue_london = q1 * p1
    revenue_birmingham = q2 * p2
    revenue_nottingham = q3 * p3

    avg_quantity = (q1 + q2 + q3) / 3
    avg_revenue = (revenue_london + revenue_birmingham + revenue_nottingham) / 3

    print("Spare Parts Sales Report")
    print(f"London: Quantity = {q1}, Revenue = €{revenue_london:.2f}")
    print(f"Birmingham: Quantity = {q2}, Revenue = €{revenue_birmingham:.2f}")
    print(f"Nottingham: Quantity = {q3}, Revenue = €{revenue_nottingham:.2f}")
    print(f"Average Quantity Sold = {avg_quantity:.1f}")
    print(f"Average Revenue = €{avg_revenue:.2f}")

report(120, 150, 100)