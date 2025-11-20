'''Question 16 
Write a program that takes an array of positive and negative numbers [5, -3, 8, -1, 0, 7, -4, 2] 
and uses a loop to separate them into two new arrays: one containing only positive numbers 
and one containing only negative numbers. '''


Array=[5, -3, 8, -1, 0, 7, -4, 2] 
ArrayPositive = []
ArrayNegative = []
for num in Array:
    if(num < 0):
        ArrayNegative.append(num)
      
    elif(num >= 0):
        ArrayPositive.append(num)
      

print(ArrayNegative)
print(ArrayPositive)