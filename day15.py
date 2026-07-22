'''num =0
num_1 = 1
any = int(input("enter a number: "))
print(num,num_1,end=" ")
for i in range(1,any+1):
    num2 = num + num_1
    num = num_1
    num_1 = num2
    print(num2,end=" ")

Amstrong = int(input("enter a number: "))
total = 0
length_ = len(str(Amstrong))
for j in str(Amstrong):
    total += int(j) ** length_
if total == Amstrong:
    print(f"{Amstrong} is Amstrong number")
else:
    print(f"{Amstrong} is not a Amstrong number")

num =int(input("enter the number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divi by 3 and 5")
else:
    print("Not")

num = 100
for j in range(1,num+1):
    if j % 3 == 0 and j % 5 == 0:
       print(f"{j} is divi by 3 and 5")

any = [34,67,56,2,3,7]
def sum_even(any):
    total = 0
    for j in any:
        if j % 2 == 0:
            total += j
    print(total)
sum_even(any)

Lambda Function
---------------
->A Lambda function is a small anonymus function
->Thiss lambda function can take n number of arguments but can only have one expression

syntax: lanbda keyword (arguments): expression


an = lambda a,b:a*b
print(an(5,6))

an = lambda a,b:a+b
print(an(5,6))

'''





























