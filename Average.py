Numbers = [10, 23, 45, 67, 89, 12, 34, 56]
total = 0
for num in Numbers:
    total +=num
average = total / len(Numbers)
print("The average is:", average)
if average > 50:
    print("The average is above 50")
else:
    print("The average is 50 or below")