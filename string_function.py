# The function upper() and lower() allow you to quickly change the case of a string to all in Uppercase & Lowercase respectively
print('SmArTpHoNe'.lower())  # O/P is smartphone
print('SmArTpHoNe'.upper())  # O/P is SMARTPHONE

# upper() and lower() function can only be used on strings
# The function that only work on certain object(lists, string etc) are called using dot(.) notation

# The capitalize() function will save you time when you need to convert the first character of a string to uppercase, while making the remaning characters lowercase
print('sMaRtPhOnE'.capitalize())  # O/P is Smartphone

# String are immutable & function wont change them. You will need to store the modified string in a variable to keep it
item = "smartwatch"
print(item.upper())   # O/P is SMARTWATCH
print(item)           # O/P is smartwatch
item_2 = item.upper()
print(item_2)         # O/P is SMARTWATCH

# The find() function checks if a character( or a pattern of characters) is present in a string. The function returns the index(position) of the given value.
# If the given value is present multiple times, the function will return the first occurrence(The lowest index)
print('Bee'.find('e'))  # O/P is 1

# Its called using a dot notation
# The find() will return an error if you dont include an argument between the parenthesis
# The find() will return -1 if the value can't be found in the string

print("robot".find("A"))   # O/P is -1