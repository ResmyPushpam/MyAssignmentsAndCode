person={"name":"Rachu","age":25,"city":"New York"}
try:
    print(person["country"])
except KeyError:    
    print("Error: The specified key does not exist in the dictionary.")
