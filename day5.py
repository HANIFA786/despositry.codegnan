'''-->List  is a collection of different data types and it is represented by [] separated by coomma


any = [1"Python is a language",[2,"this is 5th class",3],56]
print[any[2]]                               

any = [1,"Python is a language",67,68,[34,["This is python class"],78,"I'm looking for good bat",[2,"this is 5th class",3],56]]
print(any[4] [1] [0] [12])

'Mutuable'  
so = "Pyhton is a language"
print(so.replace("Python", " Java"))
print(so)


so = "Python is a language"
print(so.replace("Python", " Java"))
print(so)

any = [5,3]
any.append(3)
print(any)


methods
1. append()
-----------------------------------------
This is method is used to add new item into list, but it will add the given value index position

syntax: variable_name.append(item)

an = [1,2,3,4]
an.append(78)
print(an)
an.append([0,98,78,56])
print(an)


2. Extend
---------------------------------------------------------------------------------------

This method is also used to add new items into list, but in this extend add as each position to each index in the list and extend only takes iterables like strings list



syntax : variable_name.extend(item(iterables))

any = [1,2]
any.append("Python")
any.extend("Python")
print(any)


3. Pop
--------------------------------------------------------------
This is used to delete an item from the list, this pop() remove the value based on the index position mentioned in the parameters

if nothing is mentioned in the parameter, it will remove last index position value


syntax: variable_name.pop(index position)

any = [1, 2, 3,4]
any.pop(3)
print(any)

4.remove()
-------------------------------------
This is used to delete the items in the list but directly removes() the value
if we give the 3 to delete in the list 3 will be deleted

syntax: variable_name.remove(value)

any = [1, 2, 3, 4]
any.remove(3)
print(any)


5. slicing ()
---------------------------------------------------------------------------------------------------------------------

This is used to get the particular  part of a list, string or tuple
this work is based on index position

syntax:  variable_name[starting index : ending index]

any = [1, 2, 3, 4, 5, 6, 7,]
print(any[3:5])


len()

---------------------------------------------------------
Method is used to find the number of items present in the list

syntax  len(variable)


any = "Python is a language"
print(len(any))'''








































