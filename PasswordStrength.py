Password= "P@ssw0rd"
if (len(Password) >= 8 and
    any(char.isupper() for char in Password) and
    any(char.islower() for char in Password) and
    any(char.isdigit() for char in Password) and
    any(char in '!@#$%^&*()-_+=' for char in Password)):
    print("The password is strong.")
else:
    print("The password is weak.")
    print("Password must be at least 8 characters long, contain upper and lower case letters, digits, and special characters.")