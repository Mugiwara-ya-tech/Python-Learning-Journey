# Function are reusable block of code for specific task.
# A function contains the code to perform a task to use this code you just need to call the function name.

# Function require information to be passed in order for the task to be completed, we pass information into function as arguments
print("New Message")

# Argument go inside parenthesis() after the function name.

# The range() function takes in a number as an argument

# A functin can take multiple arguments
print("Your seat:", 4)  # O/P is Your seat: 4

# The print function can take argument from different data type
# Multiple argument in a function are separated with a comma

print("country:","Germany")  # O/P is country: Germany

# Function can take operation as arguments the print() function can accept math, logical and comparison operations

# You can use value stored in variables as arguments
balance = 304
print("Your balance is:", balance)   # O/P is Your balance is: 304

# A function can be argument for another function
print(type("world"))

# Your code will result in error if you pass the incorrect data type as an argument. Some function require specific data type as arguments
'''
for eg
the int() function won't be able to convert non-numeric character into number & it will result in an error
'''
print(int(5.5))       # O/P is 5
print(int("5"))       # O/P is 5
print(str(5))         # O/P is 5
print(int('pencil'))  # Error