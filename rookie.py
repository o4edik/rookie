

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# Write your code here.
# y = ((hour*60) + mins + dura) // 60
# print("end time: ", y - y%1, ":", (y*60)%60 )
# Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# largest_number = max(number1, number2, number3)
#
#
# # Print the result
# print("The largest number is:", largest_number)



# name = input("Plant name: ")
#
# if name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif name == "spathiphyllum": print("No, I want a big Spathiphyllum!")
#
# else:
#     print("Spathiphyllum! Not", name, "!")



income = float(input("Enter the annual income: "))
# Write your code here.
if income <= 85528:
    tax = (income * 18)/100 - 556.02

elif income > 85528:
    tax = 14839.02 + (((income - 85528)*32)/100)

tax = round(tax, 0)

if tax < 0:
   tax = 0.0

print("The tax is:", tax, "thalers")










