'''Question 8
Create an array of 10 random 
numbers between 1 and 100.
Write a loop to calculate and 
display the average (mean) of these numbers.
'''
'''
1.Empty List Array
2.declare a list using range, number from 1 to 10
3. iterate through the list and generate the randomn number
4.Append the random number to List Array
'''
import random
a = []
count=0
ListArray = list(range(10))
count=len(ListArray)
'''print(f"count is {count}")'''
for item in ListArray:
    x = random.randint(1,100)
    a.append(x)
    for item in a:
        item+=item
        
print(item/count)

    
        

    
    
      