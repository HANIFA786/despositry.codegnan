'''
set data type
-----------------------------

Set is collection of unordered elements or unique elements unlike list or tuple set is not permiteed duplicates inside it.


sn = {1,2,3,2}
print(sn)

Methods-------------------

add()------------ to the given set it will gone add the number and it is mutuable

syntax: varibale_name.add(item)

sn = {1,2,3,2}
sn.add(4)
print(sn)
-------------------------------------------------------------------------------------------------------

remove()-------------This method is used to delete an item in the set
syntax-----> variable_name.remove(value)

sn = {1,2,3,2}
sn.add(4)
print(sn)
sn.remove(3)
print(sn)

-------------------------------------------------------------------------------------------------------
pop()
this is also used to delete element in the set, but we can not specify the element and also it will delete the first number in the set.

syntax: variable_name.pop(no arguments)

sn = {1,2,3,4,5}
sn.pop()
print(sn)

------------------------------------------------------------------------------------------------------------

clear()--------this method is used to delete all elements in the set
syntax: variable_name.clear()

sn = {1,2,3,4,5}
sn.clear()
print(sn)
------------------------------------------------------------------------------------------------------------

update()-----------------to the given set it will gone add the number and it is mutuable but it cqan add more than one element

syntax: variable_name.update([elements])

sn = {1,2,3,4,5}
sn.update([4,5,6])
print(sn)
---------------------------------------------------------------------------------------------------------------

union
this method will return a set all elements from both sets, but not duplicates

syntax: set_1.union(set_2) or set_1| set_2

sn = {1,2,3,4,5}
vn = {2,4,6}
sn.union(vn)
print(sn.union(vn))
--------------------------------------------------------------------------------------------------------------

intersection()-----------------this method will give only the common elements from both sets

syntax: set_1.intersection(set_2) or set_1 & set_2

sn = {1,2,3,4,5}
vn = {2,4,6}
print(sn.intersection(vn))
print(sn & vn)
--------------------------------------------------------------------------------------------------------------

difference()------this method is used get the different elements from both sets 

syntax: set_1.difference(set_2) or set_1 & set_2

sn = {1,2,3,4,5}
vn = {2,4,6}
print(sn.difference(vn))
print(sn - vn)
---------------------------------------------------------------------------------------------------------------


type convertions---------------

converting one data type into another data type

int---> string to float

a = 8
b = str(a)
print(b)
print(type(b))
-----------------------------------------------



float---> string to int

z = 56.78
d = int(z)
g = (z)
print(g)
print(type(g))
------------------------------------------------
 
c = "67.78"                    
i = float(c)
print(i)
print(type(i))
 
string-----> int, float, list, tuple
down program

 for list tuple 
c = "67.78"                    
i = tuple(c)
print(i)
print(type(i))

-------------------------------------------------
this is for str 

r = [1,2]
print(str(r))
for j in r:
    print(j)


r = [1,2]
u = tuple(r)
print(u)
print(type(u))'''




















