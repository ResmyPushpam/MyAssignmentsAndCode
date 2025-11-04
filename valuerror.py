try:    
    value = int(input("Enter Your Age: "))    
    print("Your age is:", value)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer for age.")