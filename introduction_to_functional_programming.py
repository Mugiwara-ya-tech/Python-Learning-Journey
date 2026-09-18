# You can assign a function to a variable
def welcome(name):
    return "Welcome,"+ name
greet = welcome
print(greet("Bob"))    # O/P is Welcome,Bob

# Function can take other function as arguments
def welcome(name):
    return "Welcome,"+name

def process_user(name,func):
    return func(name)

print(process_user("Alice",welcome))    # O/P is Welcome, Alice

# The function that operate with other functions that is take another function as an argument or return a function are called Higher Order Function

# A pure function is a function that gives the same result every time you give it the same inputs & it doesn't affect anything outside of the fuction
def total(price,count):
    return price*count

# The function is impure if it depends on any external state that is modifies or that affect its output. This include changing variables or altering input arguments, such dependencies makes the fuction behaviour unpredictable and dependent on the context in which it runs
products = ['pen','scissor','paper']
def add_item(products, item):
    products.append(item)
