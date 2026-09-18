# The sum() function only works with iterable containing numericl data type (int or float)
prices = [250,300,"240",400]
total = sum(prices)
print(total)    # O/P is It will give Type Error

# Exception can often be predictable. To handle them & prevent program failure you can use try/except statement.

# The try block holds code that might cause an exception. If an exception occur execution of the try block stops & the except block is execeuted allowing the program to continue reunning.
prices = [250,300,"240",400]
try:
    total = sum(prices)
    print(total)
except TypeError:
    print("Invalid data type")
print("Happy Shopping")      # O/P is Invalid data type
                             # O/P is Happy Shopping

# When you specify only one type of exception to be handled other type of exception will not be covered. If these other exception occur the program execution will fail
colors=["Red","Yellow","Green"]
try:
    print(colors[10])
except NameError:
    print("Error")
print("Happy Shopping")     # O/P is Error

# You can have multiple except block to handle each possible exception specifically
# You can choose not to specify the exception type which allow handling of any exception that may occur. While this approach is easier the downside is that the error message may not be as clear and helpful

# Exception are very helpful when your program interacts with user input. While you cant control what a user input you can control your programs behaviour when the input doesn't match the expected format.
price = input()
try:
    price_value=int(price)
except ValueError:
    print("Please enter a number")  # O/P Hi, Please enter a number

# You can use the finally statement to perform an operation after the try/except block, no matter if an exception occured or not
prices = [559,879,"N/A",349]
try:
    print(sum(prices))
except TypeError:
    print("check the prices")
finally:
    print("Need help? Contact us")    # O/P is Check the prices, Need help? Contact us

# The else statement can be used in conjuction with the try/except block & will execute only when no error occur in the try block
books = ['Harry Potter','Dune','Emma']
try:
    choice = books[1]
except IndexError:
    print("Out of range")
else:
    print(choice + "is a great choice!")   # O/P is Dune is a great choice

# You can trigger your own exceptions based on specific condition using the raise statement. This will immediately stop the program execution & indicate on error has occured
print("Rate from 0 to 10")
rate = 15
if rate > 10 or rate < 0:
    raise ValueError     # O/P is ValueError

# To make the exception more helpful for the program user you can add a message describing the error
rate = 15
if rate>10 or rate<0:
    raise ValueError("Rate from 0 to 10")    # O/P is ValueError: Rate from 0 to 10

