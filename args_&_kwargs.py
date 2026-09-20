# If the number of argument of your function is unknown and unpredictable you can always use an iterable as an argument.
def total(numbers):
    result = 0
    for i in numbers:
        result += i
    return result
nums = [1,2,3,4,5]
print(total(nums))    # O/P is 15

# *args allow you to provide any numbers of arguments without the need to create a list before calling the function each time
def total(*args):
    result = 0
    for arg in args:
        result += arg
    return result
print(total(1,2,3,4,5))   # O/P is 15
print(total(1,2,3,4,5,6,7))   # O/P is 28
print(total(1,2,3))    # O/P is 6

# *args receives argument as a tuple, which can be used inside the function
# You need to use the unpacking operator * before args. This operator inform python that the argument is an iterable and should be unpacked to receive its value as individual arguments.

# Note: The args is just a name. You're not required to use the name args. You can choose any name

#     def <func> (<argument>,<*args>)


# When defining a function with both regular arguments and *args the regular argument must come before * args in the function definition
def show_items(category,*items):
    print("Category:"+ category)
    for item in items:
        print(item)
show_items("Electronics","Laptop","Smartphone","Tablet")

''' O/P is 
Category:Electronics
Laptop
Smartphone
Tablet
'''

# The first line of the function definition, which includes the function name and its parameter is called function signature

# Python allow you to pass keyword arguments using **kwargs. In this case **kwags receives argument in the form of a dictionary consisting of key:value pairs

#     def <func>(<arguments>,<*args>,<**kwargs>)