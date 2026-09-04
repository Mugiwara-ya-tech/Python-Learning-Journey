# To use your own function you need to define them first
# Once a function has been defined you can call it as many times as you need

def greet():
    print("Hello from a function")
    print("Have a great day")
greet()            # O/P is Hello from a function
                   # O/P is Have a great day

# Use def followed by a name to define a new function
# The body of a function contain the reusable code that is executed when the function is called. The code for the body of a function must be indented
# When a function is defined you need to make sure parenthesis() are added after the name. A colon(:) must be added at the end of the definition line

# You can define function that takes any number of arguments(including zero). Argument are put inside the parenthesis() following the function name
# A function might require argument to complete its task.

def personal_greet(name):
    print("Hello",name)
    print("Have a great day")
personal_greet("Sarah")
personal_greet("Henry")

'''
O/P is 
Hello Sarah
Have a great day

Hello Henry
Have a great day
'''

# A function must be defined before they are called
# A function can take as many argument as needed to complete the task

# When calling a function you need to use the same number of argument that have been defined in the same order
def bmi(weight,height):
    index = weight/(height*height)
    print(index)
bmi(56,180)