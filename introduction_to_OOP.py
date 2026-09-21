# In OOP blueprint are referred to as classes and the instances are known as objects.
# In python you can define a class by using the class keyword followed by the class name and a colon
# Attribute are the properties that define an object individuality within a class
# To add a attribute to a class you must define the __init__ method. This method first parameter is always self, which represent the instance of the class. Following self you specify the attributes you wish to include. Then inside the function you assign values to the initialized object attributes setting their initial state

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
my_car = Car("Audi","Yellow")

# After an object is created you can access its attribute by using the dot . notation with the variable holding the object

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
my_car = Car("Audi","Yellow")
print(my_car.brand)      # O/P is Audi
print(my_car.color)      # O/P is Yellow

# In addition to attribute you can add custom behaviours to a class by defining function within it. These function known as methods should include the 'self' parameter to interact with the class instances. You can call these methods using the dot . notation, similar to how you access attributes

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def honk(self):
        print("Beep beep!")
my_car = Car("Audi","Yellow")
my_car.honk()

# The main difference between function and methods is that function are independent and can be called on their own, while methods are objected with a class and can be called only with its instance. This mean that you can't call a method wihtout having the instances of a class where that method is defined.
# Everything in python including functions is an object