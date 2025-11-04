try:
    x=int(input("Enter a number: "))
    y=10/x
    print("Result:", y)
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")