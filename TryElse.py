try:
    val=int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print (f"You entered: {val}")

