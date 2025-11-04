try:
    number = int(input("Enter a number to divide 10 by: "))
    result = 10 / number    
    print("Result:", result)    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")        
finally:
    print("Execution completed.")