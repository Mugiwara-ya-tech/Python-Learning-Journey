# To create a module write the desired code and save that in a file with .py extension
# calc.py
def add(x,y):
  return (x+y)
def subtract(x,y):
  return (x-y)

# This is all that is required to craete a module

# IMPORT MODULE
# Module can be used in another file using the import statement. When python sees an import, it loads the module if it exists in the interpreters search path

# Its syntax is 
#       Import module

import calc
print(calc.add(10,2))    # O/P is 12

# Type of import statements

# 1. Import from module
# This allow importing specific functions, classes or variables rather than the whole module
from math import sqrt, factorial
print(sqrt(16))        # O/P is 4.0
print(factorial(6))    # O/P is 720

# 2. Import all names
# * import everything from a module into the current namespace
from math import *
print(sqrt(16))        # O/P is 4.0
print(factorial(6))    # O/P is 720

# 3. Import with Alias
# You can shorten a module name using as
import math as m
print(m.pi)      # O/P is 3.1415

# TYPE OF MODULES
# Python provides several kind of modules. Each types plays a different role in application development

# 1. Built-in Modules
# These come bundled with Python and require no installation- eg math,random,os
import random
print(random.randint(1,5))    # O/P is 4

# random.randint() returns a random number within the given range

# 2. User-Defined modules
# These are modules you create yourself such as calc.py
import calc
print(calc.subtract(20,5))   # O/P is 15

# The module is created manually and then imported into another script

# 3. External(Third party) Modules
# These modules are installed using pip
# for eg: NumPy, Pandas, Requests
import requests
r = requests.get("https://example.com")
print(r.status_code)    # O/P is 200

# requests is installed separately (pip installed requests) and provides HTTP utilities

# 4. Package modules
# A package is a directory containing multiple modules, usually with an __init__.py file
mypkg/
  __init.py__
  calc.py
  utils.py

using a module from a package
from mypkg import utils
print(utils.some_func())

# Calls a function named some_func(), the output will be whatever that function returns
# if utils.py contain something like
def somefunc():
  return "Hello"

# The O/P is Hello

# LOCATING A MODULE
# Python searches for modules in a predefined list of directories known as the module search path. You can view this list using sys.path
import sys
for p in sys.path:
  print(p)

'''
O/P is
/home/guests/sandbox
/usr/local/lib/Python 313.zip
/usr/local/lib/Python 313
/usr/local/lib/Python 313/lib-download
/usr/local/lib/Python 313/site-packages
pr
