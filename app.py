from addition import add
from subtraction import minus
from multiplication import multiply
from division import divide

print("Welcome to the simple calculator.")
print("Please select one of the following: ")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Subtraction")

is_valid = False

while not is_valid: 
    selection = input("Please enter your calculation choice:\n")
    num1 = input("Please enter your first number:\n")
    num2 = input("Please enter your second number:\n")
try:
        selection = int(selection)
        is_valid = "1","2","3","4"
except ValueError:
        print("Not valid selection")
if selection == "1":
    add
elif selection == "2":
    minus
elif selection == "3":
    multiply
elif selection == "4":
    divide

print("Your Result:\n {}".format(return(num1,num2)))