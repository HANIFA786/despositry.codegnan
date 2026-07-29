'''
MOdules
-------
->A module is a file containing python code such as:
-variables
-Functions
-Classes

import module
print(module.add(5,10))
print(module.sub(5,10))
print(module.div(5,10))
print(module.mul(5,10))
print(module.power(5,10))


Modules help us:
->Reuse of code
->Reduce code duplicate

Types of modules
----------------
->User define  modules
ex:
import module
print(module.hello_world())
print(module.module1())

->In-built modules
-os
-math
-sys

->To use all this modules, we have to import with module name

Ways to import modules
----------------------
1.using Alias name
ex:
import module as my
print(my.hello_world())
print(my.module1())

2.import entire module
ex:
import module
print(module.hello_world())
print(module.module1())

3.import all functions
4.Import specific function

math module
-----------

import math
print(math.sqrt(49))
print((math.sin(1/2))
print(math.factorial(49))     

sys module
----------
->sys module is system-specific parameters and function
ex:
import sys
print(sys.version)
print(sys.path)

random module
-------------
ex:
import random 

otp = random.randint(1000,9999)
print("your otp is", otp)
'''





























