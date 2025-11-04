original= "python"
reversed= ""
index= len(original) - 1
while index>=0:
    reversed += original[index]
    index -= 1
print("Reversed string:", reversed)