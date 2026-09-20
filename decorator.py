# In python function can be nested. This mean you can define a function inside another function body
def outer_function():
    print("Hello from the outer function")
    def inner_function():
        print("Hello from the inner function")
    inner_function()
outer_function()

'''
O/P is 
Hello from the outer function
Hello from the inner function
'''

# You can also return the result of the nested function directly from within the body of the parent function
def greet(name):
    print("Hey," + name)
    def account():
        return "Your account is created!"
    message = account()
    return message
print(greet("Bob"))    # O/P is Hey Bob, Your account is created

# Imagine you have a function that generates a message. Your goal is to create another function that takes this original function as an argument and converts the original message into uppercase without altering the original function code.

# These function are known as decorators. In the code below the uppercase() function acts as a decorator and the wrapper() function represent the modified (or decorated) version of the greet() function.
def greet():
    return "Welcome!"
def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper
greet_upper = uppercase(greet)
print(greet_upper())     # O/P is WELCOME!

# You can apply a decorator to a function using the @sign. It improves the code readability and provides a clean separation between the function and its decoration
# When a function with a decorator is called it automatically includes the behaviour defined in the decorator.

def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"
print(greet())    # WELCOME!

# You can apply the same decorator to several different functions