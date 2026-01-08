# 5.2 Use a single for loop to display a rectangle of asterisks with a given height and a given width.
height = int(input("Enter height:"))
width = int(input("Enter width:"))
for i in range(height):
    if i == 0 or i == height - 1:
            print('*' * width)
    else:
          print('*' + ' ' * (width - 2) + '*')