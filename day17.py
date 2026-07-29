'''
Generators
-----------
->Generatior in a python is enable lazy evalution for producing sequence of values efficiently.
->they differ from regular functions by execution and resuming on demand.
->Generators create iterators that yield values on at a time using the yield keyword

Functions VS Generators
-----------------------
->Regular functions execute fully upon call and return a single value,terrminating afterward.
ex:
def add(num,num_2):
    print(num + num_2)
add(5,6)
->Generators use yield to produce multiple value lazily,acting like iterators without building the
entire sequence in memory.

def count_(num):
    i = 1
    while i <= num:
        yield i
        i += 1
Gene_ = count_(3)
print(next(Gene_))
print(next(Gene_))
print(next(Gene_))

Yield
-----
->Yield pauses the generator function, saves its state(local variable,position), and returns the yielded value to the caller.

Next
----
->This advances the generator by exxecuting untill the next yield,returing that value, subsequent call resume from there.

def message_gen():
    yield "First message"
    yield "Second message"
    yield "Done"
gen_ = message_gen()
print(next(gen_))
print(next(gen_))
'''

def value_(num):
    i = 0
    while i <= num:
        yield i
        i += 1
        i =+ num
Gene_ = value_()
print(next(Gene_))
print(next(Gene_))
print(next(Gene_))






























