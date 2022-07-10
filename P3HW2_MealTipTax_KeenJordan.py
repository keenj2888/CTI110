# CTI-110
# P3HW2 - MealTipTax
# Jordan Keen
# Date: 06/24/2022
cost = float(input("Please enter cost of meal: "))

tip = float(input("Enter tip amount of 15, 18, or 20: "))

if tip ==15 or tip == 18 or tip == 20 :
    print("sucess")

else:
    print("error")
print()
print("Meal price: ",cost)
tax = 6.0
print("Tax: ",tax)
print("Tip: ",tip)
total = cost+tip+tax
print("Total", total)
