# Creating a list from scratch can sometimes be time-complexing, requiring you to manually write all the items or iterate through them with a loop.

# Lets imagine you need to create a list containing numbers frmo 1 to 50, Here is the code we would write
nums=[]
for x in range(1,51):
    nums.append(x)
print(nums)      # O/P is nums = [1,2,3,......,50]

# You need to create a empty list and then add each item by looping through a range.

# List comprehensions are useful shorthands for such operations. They offer a shorter & more readable way to create lists with various settings using just a single line of code.

nums = [ x for x in range(1,51)]
print(nums)     # O/P is nums = [1,2,3,.....50]

# List comprehension are created using square breackets [].

''' Here is a generic syntax & structure of a list comprehensions
        <variable> = [<expression> for <item> in <iterable>]
        
<variable>: The variable that will store the newly created list.
<expression>: An expression performed on each item. If no specific action is needed the item itself is used.
<item>: The current item being processed.
<iterable>: Any iterable object such as ranges, list, string, tuples & sets.
'''

# You can apply any expression to each item in the list being created with a list comprehension
nums = [x*2 for x in range(10)]
print(nums)     # O/P is [0,2,4,6,8,10,12,14,16,18]

# You can use a list as the iterable in a list comprehensions
tags = ["travel","vacation","journey"]
hashtags = ["#"+x for x in tags]
print(hashtags)     # O/P is ["#travel","#vacation","#journey"]

# You can incorporate a condition into a list comprehension placed after the iterable
users = ["Branson","Emma","Brian","Sophia","Bella","Ethan","Ava","Benjamin","Mia","Chloe"]
group =[ x for x in users if x[0] == "B"]
print(group)    # O/P is ["Brandon","Brian","Bella","Benjamin"]