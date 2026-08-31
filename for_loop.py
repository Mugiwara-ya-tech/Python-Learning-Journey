# A for loop is used to execute the same instruction over and over again a specific number of times.

# The for loop begins with the keyword "for". The variable "i" keeps the track of the number of iteration.


for i in range(100):
    print("Hello")

'''
    O/P:
    It will print "Hello" 100 times.
'''

# Range() generate a series of integer numbers.

''' for eg

    for i in range(10):   # Range creates the number starting from 0
        print(i)
        
    O/P:
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
'''
# You can replace i with any other variable of your choice.

for i in range(3):
        print(i)
        
print("--")
    
for something in range(3):
        print(something)
        
'''
O/P:
    0
    1
    2
    --
    0
    1
    2
'''

# The code that gets repeated in the for loop must be indented.

# Indentation is the space at the beginning of lines

# Code that is not correctly indented will result in an error.