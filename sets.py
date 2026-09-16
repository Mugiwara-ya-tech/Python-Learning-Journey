# Unlike tuples and lists, sets are unordered collections. They are created wtih {} curly brackets
guests = {"Merry","Anna","Jonathon"}

# Sets are unordered & dont support indexing or slicing.
# Sets can have duplicates which is very helpful when developer need to ensure that each item in a collection is a unique.

# Like list & tuples, sets can have values with different data types
# Sets are mutable, meaning you can add or remove items from them.

# Use the add() & remove() function each with a value as an argument to add or remove it from a set

guests = {"Anna","Mery","Jonathan"}
guests.add("Robert")
guests.remove("Mery")
print(guests)        # O/P is {"Jonathan","Anna","Robert"}

# The append() function works only with ordered collection type like lists & adds an item to the end of the collection
# Sets are unordered thats why you cant use it on them.

# The clear() function doesn't accept an argument & remove all the items from a set.
guests.clear()

# Calling the union() function return a new set with all elements from both sets, omitting duplicates
set1={"apple","banana"}
set2={"banana","cherry"}
combined_set = set1.union(set2)
print(combined_set)    # O/P is {"apple","banana","cherry"}

# The difference() function return a set containing element that are only in the first set and not in the second.
set1={"apple","banana","cherry"}
set2={"banana","orange"}
unique = set1.difference(set2)
print(unique)     # O/P is {"apple","cherry"}