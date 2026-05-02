'''
while statement

this while statement will keep on excuting untill or unless the condition becomes true
v =4
while v <=5:
     print(v)
     v +=1
------------------------------------------------------------------------------------------------------------------------------

range()

This range() will generate sequence numbers upto the limit

syntax--> range( starting, ending, step)


choice_U = int(input("Enter the limit:"))
for j in range(100,choice_U+1, 3):
    print(j)


Break

this break statement will exist if the condition becomes true, and never enetrs in to the next loops

any = ["hanifa", "areefa", "poojitha", "indrani", "mounika"]
for i in any:
    print(i)
    if i == "hanifa":
        break
---------------------------------------------------------------------------------------

Continue()

this statement will skip the particular iteration and loop goes to next iteration


any = ["hanifa", "areefa", "poojitha", "indrani", "mounika"]
for i in any:
    if i == "hanifa":
      continue
    print(i)
----------------------------------------------------------------------------------------
pass

pass is space holder, holds the space not get any syntax error

a = 9
b = 90
if a >=b:
    pass

---------------------------------------------------------------------------------------------

Nested loop

a loop inside the loop is called nested loop


for j in range(2,100):
    count = 0
    for an in range(1,j+1):
        if j %an ==0:
            count += 1
    if count ==2:
        print(f"{j} is a prime number")
    else:
        print(f"{j} is not a prime number")
    
-----------------------------------------------------------------------------------------------

































































































