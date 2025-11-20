'''Write a program that takes an array of numbers [12, 7, 19, 3, 25, 8] and uses a loop to create a 
new array containing only the numbers greater than 10. '''
numbers=[12,7,19,3,25,8]
newarray=[]
for num in numbers:
    if num >10:
        newarray.append(num)
print(newarray)
