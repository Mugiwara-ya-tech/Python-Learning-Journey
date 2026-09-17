# Mistakes in python can be broadly categorized into two types: bugs & exceptions

# Bugs are flaws or mistakes in a programs code, leading to incorrect or unintended behaviour.
# This doesn't necessarily stop the program from running to completion but it can result in wrong output or behaviours

# Exceptions are another category of mistakes in programming. These are specific error that occur during a program execution & interrupts its normal flaws when first encountered.

# Bugs dont neecssarily stop program execution while exceptions do

''' 
There are several type of exceptions in Python.

The NameError exception is raised when an unknown variable is used
name = "Anna"
print(surname)     # Variable not define

The SyntaxError exception is raised when a syntax mistake in the code is encountered
score = 85
if score >= 80
    print("passed")     # Missing :

The indexError is raised when you attempt to access an element of an iterable, ordered collections such as lists & tuples using an index that is outside its valid range
cars = ["BMW","Tesla","Ford"]
print(cars[3])

The typeError exception is raised when a function is called on a value of an inappropriate type.

The valueError exceptions is raised when a function receives a value of the correct type but the value itself is inappropriate or unacceptable.
'''