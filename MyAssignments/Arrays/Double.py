'''Write a program that takes an array of integers and uses a loop to create a new array where 
each element is doubled from the original array. For example, [2, 5, 7] would become [4, 10, 14].'''

numberArray=list(range(1,26))
doubleArray=[]
print(numberArray)
for num in numberArray:
    num=num*2
    doubleArray.append(num)
print(doubleArray)
    

