name_Password = "@admin123"
for char in name_Password:
    print(char)
    if char.isupper():
        print("This password contains an uppercase letter.")
    elif char.islower():
        print("This password contains a lowercase letter.")
        break
    elif char.isdigit():
        print("This password contains a digit.")
        break
    elif char in "!@#$%^&*()-+":
        print("This password contains a special character.")
    else:
        print("This password does not meet the criteria.")
        break