# Tuples like list are ordered collection of items created with parenthesis

b_date = (21,"May",2004)

# The items in tuples also have their indexes starting from 0.
# You can access the items in tuples just like you do with lists

# Tuples are immutable they are useful when the data stored in a collection shouldn't be accidentally modified during the program execution.

# Tuples like list can contain duplicate elements. You can use count() function to calculate the number of occurrences of an item in a tuple

score = (7,9,9,8,9)
print("# of 7:",score.count(7))         # O/P is # of 7: 1
print("# of 8:",score.count(8))         # O/P is # of 8: 1
print("# of 9:"),score.count(9)         # O/P is # of 9: 3

# Many functios used in lists can also be used with tuples as long as their purpose doesn't include modifying them

# The max() function return the maximum value in a collection
points = (12,14,9,10,9)
winner=max(points)
print(winner)   # O/P is 14


# Tuple unpacking allow for assigning tuple item to variable. The values will be assigned in the order they appear in tuple

birthday_date = (12,"August",1993)
day,month,year = birthday_date
print(day)          # O/P is 12
print(month)        # O/P is August
print(year)         # O/P is 1993

# While unpacking the number of variable should match the number of items in the tuple, otherwise the program will result in an error

# The * operator in tuple unpacking is used to gather multiple element from the tuple into a list. This is useful when dealing with tuples of unknown length

scores = (98,96,91,88,64)
winner,*rest = scores
print(winner)  # O/P is 98
print(rest)    # O/P is [96,91,88,64]

# Just like max() funtion its opposite is min()