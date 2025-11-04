ListofFruits = ('apple', 'banana', 'cherry', 'date')
itemToCheck = 'banana'
exists = False
for fruit in ListofFruits:
    if fruit == itemToCheck:
        exists = True
        break
if exists:
    print(f"The item '{itemToCheck}' exists in the tuple.")
else:
    print(f"The item '{itemToCheck}' does not exist in the tuple.")
        