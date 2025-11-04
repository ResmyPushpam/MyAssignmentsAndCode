secret=7
Guess=0
while Guess!=secret:
    Guess=int(input("Enter your guess (1-10): "))
    if Guess<secret:
        print("Too low! Try again.")
    elif Guess>secret:
        print("Too high! Try again.")   
    else:
        print("Congratulations! You've guessed the correct number.")    