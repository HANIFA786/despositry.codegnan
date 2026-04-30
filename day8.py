'''
print (type(u))

User input
-------------------

any = int(input("Enter a number:"))
print(type(any))


string data type
------------------------

an = input("Enter the word:")
print(type(an))


a,b = map(int,input("Enter two numbers:").split())
print(a)
print(type(a))
print(b)
print(type(b))

-----------------------------------------------------------

List data type
---------

CV = list(map(int,input("Enter the number:").split()))
print(type(CV))
print(CV)
-----------------------------------------------------------------

Tuple data type

AM = tuple(map(int,input("Enter the number:").split()))
print(type(AM))
print(AM)


A = 89
B = 7
print("Added A and B and the result is ",A+B)
print(f"Added a and b, the result is {A+B}")


A = 89
B = 7
print("A+ B",A+B)
print(f"A + B = {A+B}")



A = 89
B = 7
print("A+ B",A+B)
print(f"{A} + {B} = {A+B}")

--------------------------------------------------------------------------------------------

Statements-------------
|||||||||||||||             |||||||||||||||     ||||||||||||

conditions                   Control              Loop

IF                            break
nested if                     pass
if else                        Continue
elif


If statement
----------------------------------
this is used to check the condition is true or not

an = 9
if an >= 9:
    print(f"an is greater then or equal to {9}")

Else statement :
this method fall back statement, incase if statement becomes false, it will enter into else

an = 9
if an >= 9:
    print(f"an is greater then or equal to {9}")
else:
    print(f"an is not greater than {9}")


program to check two numbers less greater than or equal to


a = 12
b = 25
if a <= 12:
    print(f"a is less then or equal to {a}")
else:
    print(f"a is not less than {b}")
--------------------------------------------------
Evlave

what ever we want we will get it whether it can be string or int 

v = eval(input("Enter:"))
print(type(v))
print(v)


num = 7
num_2 = 23
if num > num_2:
    print(f"{num} is greater than {num_2}")
else:
    print(f"{num} is greaters than {num_2}")


age = int(input("Enter your age:"))
if age >= 18:
          print("You aree eligible to vote")
else:
    print(f"you have to wait {18-age} more years")


marks_ = int(input("Enter your marks:"))
if marks_ < 35:
          print("your failed")
else:
    print(f" your passed")'''


















































