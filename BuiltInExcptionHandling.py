try:
num = int(input ("Enter a number: "))
    print("You entered:", num)
    print( type(num))
    num = num**2
    print(num)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print("An error occurred:", e)
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")      
except TypeError:
    print("Type error occurred. Please check your input.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except IndexError:
    print("Index out of range. Please check your input.")   
except FileNotFoundError:
    print("File not found. Please check the file path.")
except IOError:
    print("Input/output error occurred.")
except AttributeError:
    print("Attribute error occurred. Please check your code.")
except ImportError:
    print("Import error occurred. Please check your imports.")
except RuntimeError:
    print("Runtime error occurred. Please check your code.")    
except OverflowError:
    print("Overflow error occurred. Please check your calculations.")
except MemoryError:                     
    print("Memory error occurred. Please check your code.")
finally:
    print("Execution completed.")

