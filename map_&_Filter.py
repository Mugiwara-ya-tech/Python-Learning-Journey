# The map() function applied a specified function to every element in an iterable, like list or tuples. It produces a result that can be transformed into a list using the list() function for easy viewing or further use
names = ["alice","bob","CHARLIE","dEborah"]
def capitalize(name):
    return name.capitalize()

capitalized = map(capitalize,names)

capitalized = list(capitalized)
print(capitalized)     # O/P is ["Alice","Bob","Charlie","Deborha"]

# The map function takes two arguments- an iterable and a function
#    map(<function>,<iterable>)

# The map function require the first argument to be a function and the second argument to be iterable
exam_scores = [85,62,95,40,78]
def is_passing(score):
    return score >= 70
status = list(map(is_passing,exam_scores))
print(status)     # O/P is [True,False,True,False,True]


numbers = [1,2,3]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)     # O/P is [2,4,6]

# The filter() function just like the map() function takes in a function and an iterable as arguments. The key purpose of filter() is to apply a condition specified in the provided funciton to each item in the iterable and return only those for which the function evaluates to True.
products = ["Table","Sofa","Cushion","Bookshelf","Vase"]
filtered_prod = list(filter(lambda name: len(name)==4, products))
print(filtered_prod)      # O/P is ["Sofa","Vase"]

# The filter() function is to particularly useful for extracting subset of data that meet certain criteria.

# To transform the item of an iterable: map()
# To return items that meet a condition: filter()