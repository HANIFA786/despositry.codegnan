
'''
-->Data types:they are 2 types
-->1.mutable:i can modify directly on the variable, which the data type have taken
-->eq:list,dict
-->2.immutable:where can not be modified directly on the variable assign to the data type
-->eg: int,string

integer or int:
----------------
->storing numbers or digit in the variable is called int
-->float:
->storing decimal value in the variable is called float
num_2 =87.67

indexing
--------
-->this is used to get the particular substring,item from string,
list and tuple by calling with index position

syntax
------
variable_name[index_position]'''

eq:
any="python is a programing language"  #o/p:a
print(any[10])

'''
concatenantion
--------------
-->A + acts as different way,if we are adiing 2 integers it acts like in other cases such as list,string anad tuple it act like concatenation
'''
eq:
any ="python"
so="language"
print(any+ " " +so)
num=[4,0]
num_2=[5,6]
print(num+num_2)

'''
strings or str:
---------------
->string is a collection of char that are inclosed in '',""
->it is immutable data type

methods
-------
->1.replace():
--------------
-->this method is used to replace or chage old sub string with new string
syntax
------
variable_name.replace("old string","new string")
->2.split():
----------
-->this method used to seprate the string using a substring and it will split into list such as before the substring is one index and after the
substring is another index

syntax
------
variable_name.split("substring")
--
->3.strip():
-----------
-->this method is used to remove from 1st index position or from last index position

->4.join():
----------
syntax
------
"substring".join(variable)
->5.lower():
->6.upper():
'''

->1.replace():example

any="python is a programing language"
print(any.replace("python","java"))   #it only change the given variable but it wont modify so it is called immutable

->2.split():eq
any = "python is a language"
print(any.split(" "))

->3.strip():eq
any = "python is a language"
print(any.strip("py"))

->4.join():
any = "python is a language"
print("-".join(any))

->5.lower():
any = "Python is a lANguage"
print(any.lower())

->6.upper():
any = "Python is a lANguage"
print(any.upper())

num=int(input())
print(f"{num}is a odd number")
if num%2:
    print("even")
else:
    print("odd")
