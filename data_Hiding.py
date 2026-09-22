# Data Hiding is a key idea in making code with objects safer and cleaner. It mean keeping some part of an object private so that onlycertain part of your code can change them. This help prevent mistakes and keeps your code easy to manage.
# Consider the Car class provided below After creating an instances of this class, you can access and modify its attribute as well as call its methods.

class Car:
    def __init__(self,model,year,odometer):
        self.model = model
        self.year = year
        self.odometer = odometer
    def describe_car(self):
        print(self.year, self.model)
    def read_odometer(self):
        print("Odometer:",self.odometer,"miles")
my_car = Car("Audi",2020,15000)
my_car.describe_car()       # 2020 Audi
my_car.read_odometer()      # Odometer = 15000
my_car.odometer = 20000
my_car.read_odometer()      # Odometer = 20000

# In programming sometimes its crucial to protect certain class attributes & methods fom being accessed outside the class. This is called data hiding & ensure the integrity and security harmful modifications.
# In python data hiding has two levels. The first involves prefixing an attribute with a single underscore_, signaling it mean for internal use and should be viewed as 'protected'

class Car:
    def __init__(self,model,year,odometer):
        self.model = model
        self.year = year
        self.odometer = odometer

    def describe_car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print("Odometer :", self._odometer, "miles")

my_car = Car("Audi",2020,15000)
my_car.describe_car()               # 2020 Audi
my_car.read_odometer()              # 15000 miles

# Attribute with a single underscore are accessible but considered protected by convention signaling they're for internal use and should be accessed cautiously outside the class

# To access a protected attribute outside of the class, use the single underscore prefix as thats part of the attribute name

class Car:
    def __init__(self,model,year,odometer):
        self.model = model
        self.year = year
        self.odometer = odometer

    def describe_Car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print("Odometer :", self._odometer, "miles")

my_car = Car("Audi",2020,15000)
print(my_car._odometer)

# The next level of data hiding involves making an attribute private. This is achieved by prefixing the attribute name with two underscores. In this case unlike protected attributes this is not jsut a convention it limits its access outside the class through name mangling, enhancing data protection and enncpasulation. This method is used for sensitive or internal data, strong discouraging external access.

class Car:
    def __init__(self,model,year,odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer

# Accessing a private attribute with double underscores from outside the class causes an error, but its accessible within class methods. This demonstrates encapsulation, protecting sensitive data from external access and ensuring its only reachable via specific methods, aligning with object oriented programming principles

class Car:
    def __init__(self,model,year,odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer

    def describe_car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print("Odometer :",self.__odometer,"miles")

my_car = Car("Audi",2020,15000)
my_car.read_odometer()
print(my_car.__odometer)

# Accessing a private attribute directly from outside its class is generally discouraged in python. However Python employs name mangling for private attributes which mean you can access them using a specific naming convention from outside the class if necessary

class Car:
    def __init__(self,model,year,odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer

    def describe_car(self):
        print("Odometer :", self.__odometer, "miles")

my_car = Car("Audi",2020,15000)
print(my_car._Car__odometer)     # O/P is 15000

# Note: However this approach should be used sparingly as it bypasses the encapsulation principles intended by making the attribute private.
# You can also designate methods as protected or private following the same convention as with attribute. Protected methods are prefixed with a single underscore and can be accessed within the class and its subclasses

# However private methods marked by a double underscore, cant be directly accessed from outside the class

class Car:
    def __init__(self,model,year,odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer

    def _describe_car(self):
        print(self.year, self.model)

    def __read_odometer(self):
        print("Odometer :", self.__odometer, "miles")

my_car = Car("Audi",2020,15000)
my_car._describe_car()
my_car.__read_odometer()