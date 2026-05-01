'''
elif statement
------------------------------------
This statement gives the options to get the result that program


Eample

marks_stu = int(input("Enter your marks:"))
if marks_stu >= 90 :
    print("A+")
elif marks_stu >=80:
        print("A")
elif marks_stu >=70:
        print("B+")
elif marks_stu >=60:
        print("B")
elif marks_stu >=50:
        print("C+")
else :
    print("failed")

------------------------------------------------------------------------------------------------------------
Nested if statement
--------------------------------------------------
if statement inside another if statement is called Nested if statement


user_SBI_info = {"ATM PIN": "7788"}
User_pin = input("Enter your ATM")
if len(User_pin) ==4:
    if User_pin in user_SBI_info['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("Pls enter the correct pin")
else:
    print("Pls enter 4 digit pin")
---------------------------------------------------------------------------------------------------------------

for statement ****************
else statemt in for

After completing all iterations this else statement will excute

any =  [23, 45, 78, 56]
for j in any :
    print (j)
else:
    print("Loop finished")



so = "madam"
empty_ = ""
for j in so:
    empty_ = j + empty_
    if empty_ == so:
        print("Palindrom")
    else:
        print("Not a Palindrom")



so = "madam"
empty_ = ""
for j in so:
    empty_ = j + empty_
if empty_ == so:
        print("Palindrom")
else:
        print("Not a Palindrom")

--------------------------------------------------------------------------------

while statement **************















































































































































































































