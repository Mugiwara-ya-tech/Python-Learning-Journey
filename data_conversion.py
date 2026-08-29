# The input() instruction always turns the user input into a string, no matter what the user enters

birth_year = input()
print(type(birth_year))  # O/P is 42, <class 'str'>

# The int() instruction convert any type of value into an integer

x = "55"
print(type(x))
y=int(x)
print(type(x))  # O/P is <class 'str'>, <class 'int'>

# The float() instruction converts value into floats

# The str() instruction converts value into strings