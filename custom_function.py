# The result of a function can be sent back with the return statement.
# This is particularly helpful when you need to continue using the result value in your program

def bmi(weight,height):
    index = weight/(height*height)
    return index
patient_5 = bmi(61,1.83)
print("underweight:",patient_5 < 18.5)          # O/P is underweight: True

patient_7 = bmi(75,1.74)
print("underweight:",patient_7 < 18.5)          # O/P is underweight: False

# A function can return multiple return value

def rect(length,width):
    area = length*width
    perimeter = 2*length + 2*width
    return area, perimeter

x,y = rect(50,100)
print(x,y)

# Python allow function argument to have default values
# If the functions is called without the argument the argument gets it default value

def greet(name="Guest"):
    print("Welcome",name)
greet()              # O/P is Welcome Guest
greet("John")        # O/P is Welcome John

# Add the default value with the equal = sign to make the argument optional
# The default value is used only if no other value has been passed as an argument when the function is called