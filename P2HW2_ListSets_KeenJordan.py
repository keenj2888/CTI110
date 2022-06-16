# CTI-110
# P2HW2 - List and Sets
# Jordan Keen
# Date:06/16/2022
#
mylist=[]

num=float(input("Enter num 1: "))
mylist.append(num)
num=float(input("Enter num 2: "))
mylist.append(num)
num=float(input("Enter num 3: "))
mylist.append(num)
num=float(input("Enter num 4: "))
mylist.append(num)
num=float(input("Enter num 5: "))
mylist.append(num)
num=float(input("Enter num 6: "))
mylist.append(num)
print()
print("Created list")
print(mylist)

print("Smallest number in list: ",min(mylist))
print("Largest number in list: ",max(mylist))
print("Sum of the numbers in list: ",sum(mylist))
print("Average of numbers in list: ",sum(mylist)/len(mylist))
print()
print("Created set")
print(set(mylist))

input("Press enter to exit")
