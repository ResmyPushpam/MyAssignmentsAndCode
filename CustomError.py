def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print(f"Your age is: {age}")

# Main program (outside the function)
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as ve:
    if "invalid literal" in str(ve):
        print("Error: Please enter a valid number.")
    else:
        print("Error:", ve)
        print("Please enter a valid age.")