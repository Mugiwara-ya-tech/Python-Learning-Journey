# Inheritance is a key concept far situations where you have an existing class with defined attribute and behaviours and you need a new class that only shares these characteristics but also has its own unique one
# Inheritance allow the new class to 'inherit' properties from the existing class while adding or modifying specific features as needed.

class Animal:
    def __init__(self,name):
        self.name = name
    def move(self):
        print("Moving")
class Dog(Animal):
    def bark(self):
        print("Woof!")
my_dog = Dog("Bob")
print(my_dog.name)          # O/P is Bob
my_dog.move()               # O/P is Moving
my_dog.bark()               # O/P is Woof!

# A class from which other are inherited is known as a superclass or parent class. Conversely a class that inherits from another class is referred to as a subclass or child class

# What if we want to not only inherit attributes but also add specific ones to a child class? In this case we define an __init__ method in the child class.
# Use super().__init__() to inherit attributes from the parent class and then define any additional attribute as usual

class Animal:
    def __init__(self,name):
        self.name = name
    def move(self):
        print("Moving")
class Dog(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name)
        self.breed = breed
        self.age = age
    def bark(self):
        print("Woof!")
my_dog = Dog("Jax","Bulldog",5)
print(my_dog.name)          # O/P is Jax
print(my_dog.breed)         # O/P is Bulldog
print(my_dog.age)           # O/P is 5

# You can define methods with the same name in both parent and child classes but they can perform different operations. This is known as method overriding for instance consider the Animal class with a sound method. The method from Animal but override it to suit their specific needs

class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("Making a sound")
class Dog(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name)
        self.breed = breed
        self.age = age
    def sound(self):
        print("Woof!")
class Cat(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name)
        self.breed = breed
        self.age = age
    def sound(self):
        print("Meow!")
my_dog = Dog("Jax","Bulldog",5)
my_cat = Cat("Lily,Ragdoll",2)
my_dog.sound()       # O/P is Woof!
my_cat.sound()       # O/P is Meow!

# You can use the super() function if you want to call a method form the parent class while overriding it
# This is useful when you want to add some functionality to the child class method without changing the original one

def sound(self):
    super().sound()
    print("Woof!")

# Method overriding is a demonstration of another key concept in OOP - Polymorphism
# Polymorphism lets object use methods in their own way even if they share the same name

# In this eg even though each animal in the animals list may be of a different subclass the code can call sound() on each without needing to know its specific type

class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("Making a sound")
class Dog(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name)
        self.breed = breed
        self.age = age
    def sound(self):
        print("Woof!")
class Cat(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name)
        self.breed = breed
        self.age = age
    def sound(self):
        print("Meow!")
my_dog = Dog("Jax","Bulldog",5)
my_cat = Cat("Lily","Ragdoll",2)
animals = [my_dog,my_cat]
for animal in animals:
    animal.sound()     # O/P is Woof!, Meow!