Mounika_union_ac_details={"Name":"Mounika","ATM_PIN":"8008","Balance":7000,"Transaction history":[]}
print("---------------WELCOME TO UNION  BANK------------------------")
print("Please insert your card")
user_pin = input("Please enter your 4 digit pin:")
if len(user_pin) == 4:
    if user_pin in Mounika_union_ac_details["ATM_PIN"]:
        Choice_ = int(input("\n1.Withdraw \n2.Deposite: \n3.Check_Balnce \n4.Change_Pin \n5.Transaction_History"))
        if Choice_ == 1:
            Withdraw_M = int(input("Enter amout  you want to withdraw: "))

            if Withdraw_M <= Mounika_union_ac_details['Balance'] and Withdraw_M:
                Mounika_union_ac_details['Balance'] -= Withdraw_M
                print("Please wait unlike money process")
            else:
                print("Insuffient funds or change is not getable")
        elif Choice_== 2:
            deposit_m = int(input("Enter amount to deposit: "))

            if deposit_m >= 1000 or deposit_m%100 == 0:
                Mounika_union_ac_details['Balance'] += deposit_m
                print("Amount deposited successfully")
                print("Updated Balance:", Mounika_union_ac_details['Balance'])
            else:
                print("Invalid amount")
        elif Choice_==3:
             print("Available Balance:",Mounika_union_ac_details["Balance"])
        elif Choice_ == 4:
            old_pin = input("Enter old PIN: ")

            if old_pin == Mounika_union_ac_details["ATM_PIN"]:

                new_pin = input("Enter new 4 digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():

                    Mounika_union_ac_details["ATM_PIN"] = new_pin

                    print("PIN changed successfully")

                else:
                    print("PIN must contain 4 digits only")

            else:
                print("Incorrect old PIN")
        elif Choice_ ==5:
             print("\n------Transaction History------")

            if len(Mounika_union_ac_details["Transaction_History"])>0:
                for i in Mounika_union_ac_details["Transaction_History"]:
                    print(i)

            else:
                print("No transactions found")

            else:
               print("Invalid choice")
            
        else:
         print("Please enter correct pin")
else:
    print("Please enter only 4 digit pin")
