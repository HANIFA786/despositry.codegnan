'''
Functions--------------

---> This is a block of code that can be reusable
---> function can only run when it is called
---> def is used to define the function


syntax:

start like this
def func_name(): this is parameters
    ----------------
    -----------------  should start from here
func_name()------ this is called as arguments


num = 9
def even_odd(num):
    if num %2 ==0:
       print(f"{num} is an even number")
    else:
        print(f"{num} is a odd number")
even_odd(num)
even_odd(130)

Required Ar:

--> A function must called with the correct number of arguments, that means if function expects 2 arguments, we have to call function wit 2 arguments not less or not more.



def even_odd(num, num_2):
       print(num+num_2)
even_odd(8,9)

 def even_odd(num, num_2):
       print(num+num_2)
even_odd(8,9,85) in this we will get the error because we should not take 3 arguments only two argumenst should be given.
------------------------------------------------------------------------------------------------------------------------------------------------

Default Arguments:
In default values are taken from the calling function



def even_odd(name = "Hanifa"):
    print(f"hello {name}")
even_odd("Begum")
even_odd("Qwaja")
even_odd()
-----------------------------------------------------------------------------------------------
Keyword Arguments
------> Here we can send arguments with key = value syntax. By this, the order of arguments does not matter.


def even_odd(num_2,num_3,num):
    print(num+num_2+num_3)
even_odd(num=7,num_2=8,num_3=6)
    
-----------------------------------------------------------------------------------------------------

Variable Length Argument

---> Adding a star (*) before the parameter name in the function, receieve a tuple of arguments and can be items with indexes'''

def even_odd(*name):
    print(name[0])
even_odd("Qwaja", "Love","Hanifa")
















































































