try:
    age = int(input("Enter your age: "))
    
    if age >= 18:
        citizenship = input("Are you a citizen? (yes/no): ").strip().lower()
        if citizenship == "yes":
            print("You are eligible to vote.")
        else:
            print("You must be a citizen to vote.")
    else:
        print("You must be at least 18 years old to vote.")

except ValueError:
    print("Invalid input. Please enter a valid age.")