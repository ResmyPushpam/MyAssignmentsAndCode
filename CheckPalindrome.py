Enter_string = input("Enter a string to check if it's a palindrome: ")
Reverse_string = Enter_string[::-1]
if Enter_string == Reverse_string:
    print(f"{Enter_string} is a palindrome.")
else:
    print(f"{Enter_string} is not a palindrome.")
