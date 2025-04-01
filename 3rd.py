# 3rd

print("WELCOME !!")
balance = 50000

print("MENU =>\n 1.Check balance\n 2.Deposite money\n 3.Withdraw money\n 4.Exit the system..")
ch = int(input("Enter your choice="))

if ch == 1:
    print("Balance is=",balance)
elif ch == 2:
    deposite = int(input("Enter the amount to deposite="))
    new_bal = balance + deposite
    print("New balance=",new_bal)
elif ch == 3:
    withdraw = int(input("Enter amount to withdraw="))
    new_bal1 = balance - withdraw
    print("New balance=",new_bal1)
else:
    print("Exit")