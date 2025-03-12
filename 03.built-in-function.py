'''
The Python interpreter has a number of functions and types built into it that are always available.
They are listed here in alphabetical order in the following link.
https://docs.python.org/3/library/functions.html
'''

# List the all built in function
print("=======Built in function List===========")
print()
print(dir(__builtins__))

# To know about any function write the following command
print()
print("=======Definition of any builtin function========")
print(help(len))

# Example of some built-in function
print()
print("=======Example of some builtin function========")
print("No of Character of 'Python' : ",len("Python"))
print("Square of 10: ",pow(10,2)) # square or cube or any number of "to the power"
print("Max value of (1,2,3,4,5,6,7): ",max((1,2,3,4,5,6,7)))
print("Min value of (1,2,3,4,5,6,7): ",min((1,2,3,4,5,6,7)))

'''
Built in Modules:
Python built-in modules are a set of libraries that come pre-installed with the Python installation. 
It will become a tedious task to install any required modules in between the process of development 
that's why Python comes with some most used modules required. These modules provide a wide range of 
functionalities, from file operations and system-related tasks to mathematical computations and web services. 
The use of these modules simplifies the development process, as developers can leverage the built-in functions
and classes for common tasks, providing code reusability, and efficiency. 
Some examples of Python built-in modules include "os", "sys", "math", and "datetime". 

Source: https://www.geeksforgeeks.org/built-in-modules-in-python/

'''
# To get all available modules
print()
print("=======All built-in module list========")
print(help('modules'))

# To get function list of a modules
import math # for using any module we have to import it
print()
print("=======Get available function list of a module (math)========")
print(dir(math))

# some example of math module uses
print()
print("=======Example of math and datetime module========")
print("Squar root of 16: ",math.sqrt(16))
print("value of pi : ",math.pi)

import datetime
print("Today : ",datetime.date.today())
print("Time Now : ",datetime.datetime.now().time())


















