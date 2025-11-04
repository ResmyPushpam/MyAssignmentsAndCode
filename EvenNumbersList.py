ListNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
EvenNumbers = []
for number in ListNumbers:
    if number % 2 == 0:
        EvenNumbers.append(number)
print("Even Numbers:", EvenNumbers)