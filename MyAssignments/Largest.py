numbers = [3, 7, 2, 9, 4, 1, 8]
tempnum = 0  # Start with a small value

for num in numbers:
    if num > tempnum:
        tempnum = num

print("The largest number is:", tempnum)