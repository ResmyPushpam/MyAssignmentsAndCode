balance = 10000
moneyToWithdraw = 100
if moneyToWithdraw <= balance:
    balance -= moneyToWithdraw
    print("Please collect your Cash")
    print(f"Your remaining balance is: {balance}")
elif moneyToWithdraw > balance:
    print("Insuffecient Balance")
else:
    print("Invalid Input")
#ATMwithdrawal.py
# This is a simple ATM withdrawal simulation