try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f" {name} is {age} years old.")  
except Exception as e:
    print("An error occurred:", e)
