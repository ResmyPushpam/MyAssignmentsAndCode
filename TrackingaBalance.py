balance=1000;
moneyToWithdraw=950
if moneyToWithdraw <= balance:
    balance -= moneyToWithdraw
    print( f"Please collect your Cash\nYour remaining balance is: {balance}")
elif moneyToWithdraw > balance:
    print("Insuffecient Balance")
elif balance <= 50:
    print("Your balance is low")
else:
    print("Invalid Input")