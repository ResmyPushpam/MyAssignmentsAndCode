'''Given an array of numbers [5, 8, 3, 9, 3, 7, 3, 2], write a program that counts how many times 
the number 3 appears in the array. '''
ArrayNumbers=[5, 8, 3, 9, 3, 7, 3, 2]
checknum=3
count=0
for num in ArrayNumbers:
    if num==checknum:
        count+=1
print(f"There are 3 occurring ,{count} times")

