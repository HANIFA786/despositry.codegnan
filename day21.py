'''
                                      OOP'S

class
------
->class is instance or blueprint of an object
ex:
class student:  #student class
    def display(self):
        print("hello")

object
------
->object is the instance of the calss
ex:
class car:
    def brand(self):
        print("I have created a new car")

car_1 = car()
car_1.brand()

Constructor
-----------
->A constructor is a special method that executes automatically when the object is created
->(__init__)
ex:
class car:
    def __init__(self,color,Brand):
        self.color = color
        self.Brand = Brand

    def car_Brand(self):
        print(f"Brand is {self.Brand} ")

    def car_color(self):
        print(f"color is {self.color} ")

car_1 = car("Blue","BMW")
car_1.car_Brand()
car_1.car_color()

self keyword
------------
->This self refer to the current object

ex:
class student:
    def __init__(self,name,age,gender,year):
        self.name = name
        self.age = age
        self.gender = gender
        self.year = year
        
    def student_det(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.year)

    def student_year(self):
        print(self.year)
stu_ = student("aareefa",21,"female",2026)
stu_.student_det()
stu_.student_year()   


class animal:
    def __init__(self,dog,cat):
        self.dog = dog
        self.cat = cat
        
    def animal_bread(self):
        print(self.dog)
        print(self.cat)
    def animal_sound(self):
        print(self.dog)
        print(self.cat)
    
ani_=animal("husky","Persian")
ani_.animal_bread()
ani_ = animal("boww","meow")
ani_.animal_sound()


class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def cat(self):
        print(f"name of animal is {self.name}")
        print(f"sound is {self.sound}")
    def dog(self):
        print(f"name of animal is {self.name}")
        print(f"sound is {self.sound}")
name = input(" ")
animal_1=Animal(name,"meow meow")
animal_2=Animal("Dog","bow bow")
animal_1.cat()
animal_2.dog()

Encapsulation
------------
->This bunding data and the methods that works on the data inside the class, while limiting
direct access to the internal state.

name is public and can be accessed directly
Adhar is a procted,means internal use only
Pan is a priate, thiss makes direct access hard

'''
class bank:
    def __init__(self,name,Adhar,Pan):
        self.name =name
        self._Adhar =Adhar
        self.__Pan = Pan
    def Adhar_(self):
        print(self._Adhar)
    def Pan_(self):
        print(self.__Pan)
SBI_Bank = Bank("Aareefa",563600709726,"ABF0D5d7")
SBI_Bank.Adhar_()

































