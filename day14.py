#print statement
#------------------
#this print statement shows the output on the screen 


#return statement
#--------------

# sends a value back to caller or calling for the program to reuse
# def add(a,b):
#     return a+b
# result=add(2,3)
# print(result)

#inbuilt function

# len()
#-------this is used to find out the number of values present in iterables(string,list,tuple)

# max()
#-------
#this is used to get the maximum value 

# li=[1,4,2,5]
# print(max(li))

# li=["34","python","24"]
# print(max(li))


#min
#--------
#this is used to find out the minimum value
# li=["python","23","life"]
# print(min(li))

#type()
#range()

#recursive funtion
#-----------a recursive function calls itself until a base case is stops it

# def fact(num):
#     if num==0 or num==1:
#         return 1
#     return num*fact(num-1)
# print(fact(6))


def table(n):
    for i in range(1,11):
        print( f"{n} x {i} = {n*i}")
n=int(input("enter a table:"))
(table(n))
