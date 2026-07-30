'''
polymorphism
------------
->polymorphism mean "many forms",The same method, Operator or a function can perform different actions
depend upon the object or data type..

1.Method overloading
--------------------
->Method overloading is creating multiple methods with the same name but with the different parameters 

ex:
class Addition:
    def add(self, a, b=0, c=0):
        return a+b+c
obj = Addition()
print(obj.add(23,7))
print(obj.add(10,20,30))

#write  a method overloaded with a power
class power:
    def pow(self,a,b=2):
        return a**b
an = power()
print(an.pow(5))

2. Method overriding
--------------------
ex:
class animal:
    def sound(self):
        print("animal make sound")
        
class dog(animal):
    def sound(self):
        print("dog barks")
    
any = dog()
any.sound()

3.Operator overloading
----------------------
ex:
class student:
    def __init__ (self, marks):
        self.marks = marks
    def __add__(self,mark_):
        return self.marks + mark_.marks

so = student(56)
how = student(78)

print(so + how)

'''

from abc import ABC, abstractmethod

class vehical(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehical):
    def start(self):
        print("car starts with key")

who = car()
who.start()
