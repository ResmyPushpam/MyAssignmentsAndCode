ListOfNumbers = [10, 25, 3, 47, 15, 99, 4]
max_number = ListOfNumbers[0]
for number in ListOfNumbers:
    if number > max_number:
        max_number = number
print(f"The maximum number in the list is: {max_number}")   
