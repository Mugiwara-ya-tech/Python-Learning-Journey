# Dictionaries are collection type used to store data in key:value pair which are considered as items.
# They are ideal for organizing data into pair where each piece of data(value) has its unique identifier(key)

product = {
    "name":"pen",
    "color":"red",
    "price":79
}

# Dictionaries are created using {} brackets

# Key:Value pairs in a dictionary are separated by commas & they can be written on new line for a better readability.
# While strings are the most commonly used data type for keys, other immutable types can also serve as keys.
# Values can be of any data type

# Dictionaries can have duplicate value but not duplicate keys. Value with duplicate key will overwrite existing values
car = {
    "brand":"Audi",
    "model":"Q5",
    "model":"A5"
}
print(car)   # O/P is {"brand":"Audi","model":"A5"}

# Values in lists and tuples are accessed using indexes. To access value in dictionaries you need to use the keys
car = {
    "brand":"Audi",
    "model":"Q5",
    "year":2008
}
print(car["brand"])     # O/P is Audi
print(car["model"])     # O/P is Q5
print(car["year"])      # O/P is 2008

# The keys should be enclosed in square brackets

# Another way to access values in a dictionary is through the get() function
# Its called on dictionary using dot . notation and accepts the key as an argument

info = car.get("model")

# You can get all the values and key of a dictionary using the values() and keys() functions
contact = {
    "name":"John",
    "company":"Microsoft",
}
info_keys = contact.keys()
info_values = contact.values()
print(info_keys)      # O/P is dict_keys(['name','company'])
print(info_values)    # O/P is dict_values(['John','Microsoft'])

# The items() function return all the key:value pair in a dictionary
car = {
    "brand":"Audi",
    "model":"Q5"
}
info = car.items()
print(info)   # O/P is dict_items([('brand','Audi'),('model','Q5')])

# You can use keys not only to access values in a dictionary but also to change them
user = {
    "Name":"Albert",
    "Age":29
}
user["Age"] = 30
print(user["Age"])     # O/P is 30
print(user.items())    # O/P is dict_items([('Name','Albert'),('Age',30)]) 

# You can add a new items by providing a new key and assigning a value to it
user['faculty'] = "Arts"

# The update() function updates the dictionary with the items from the given argument
# The argument must be a dictionary with the item you want to update

user = {
    "Name":"Albert",
    "Age":29
}
user.update({"Age":30})
print(user["Age"])          # O/P is 30
print(user.items())         # O/P is dict_items([("Name","Albert"),("Age",30)])

# The argument for the update() function should be a dictionary meaning it should start with { & end with }

# The update() function can accept dictionaries with multiple items. If an items is new it will be added to the original dictionary

# The pop() function remove the items with the specified key name. It accepts the key of the item you want to remove as an argument.

# You can use the in operator to check if a key or a value occurs in a dictionary
car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Color":"red"
}
print("Color" in car)    # O/P is True

# To check if a value occur in a dictionary you need to use the values() function

"red" in car.values()

# You can iterate through a dictionary using a for loop. If you loop through a dictionary it will return the keys
car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Color":"Red"
}
for i in car:
    print(i)      #O/P is 
                    # Brand
                    # Model
                    # Color