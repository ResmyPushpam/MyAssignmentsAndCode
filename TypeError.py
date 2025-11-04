try:
    result = "5" + 10
    print("Result:", result)
except TypeError as te:
    print("Error:", te)
    print("Please ensure all inputs are of the same type.")
    print("Hint: You can convert numbers to strings using str().")  