# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
# TODO: Use a for loop to print each fruit in the list
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
for fruit in fruits:
  print(fruit)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count >= 1:
  print(count)
  count -= 1
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1,11):
  print(i * i)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["red", "green", "blue", "yellow", "brown"]
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
  print(random.choice(colors))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations
print(math_operations.add(3,2))
print(math_operations.subtract(6,4))
print(math_operations.multiply(2,2))
print(math_operations.divide(10,0))

# TODO: Use a while loop to create a simple calculator
while True:
  print()
  print("calculator: add,subtract,multiply,divide(or type quit to stop)")
  choice = input("what do you want to do?")
  if choice == "quit":
    print("goodbye!")
    break
  choice = input("Enter operation (add, subtract, multiply, divide): ").lower()
num1 =float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))
if choice == "add":
  print(math_operations.add(num1, num2))
elif choice == "subtract":
  print(math_operations.subtract(num1, num2))
elif choice == "multiply":
  print(math_operations.multiply(num1, num2))
elif choice == "divide":
 print(math_operations.divide(num1, num2))
else:
 print("Invalid choice, try again")