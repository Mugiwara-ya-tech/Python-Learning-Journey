# Len() stands for  length & when used on lists it returns the number of items in the list 

movies = ["Avatar","Titanic","Avengers"]
print(len(movies))    # O/P is 3

# The len() function is not only for lists. It accepts as an argument any sequence, including string

movies = "Avatar"
print(len(movies))  # O/P is 6

# Its not specific to any one particular data type or object so we dont use dot notation to call it

# The append() function adds a new item to the end of a list
# append() is called using dot notation because it specific to list

songs = ["Yesterday","Hello","Believer"]
songs.append("Imagine")
print(songs)   # O/P is ["Yesterday","Hello","Believer"]

# The insert() function allow you to add an element to a list at a specific position

items = ["book","pen","pencil"]
items.append(2,"marker")
print(items)     # O/P is ["book","pen","marker","pencil"]
print(items[2])   # O/P is marker

# Insert() takes 2 argument. The first is the index(where to insert) & the second is the item(what to insert)

# The pop() functino removes an element from a list that position indicated by the index is the only argument that the pop() functin accepts

items = ["book","pen","pencil"]
items.pop(1)
print(items)      # O/P is ["book","pencil"]
print(items[1])   # O/P is pencil