'''Create an array of 10 random numbers between 1 and 100. Write a loop to calculate and 
display the average (mean) of these numbers. '''
import random
TotalOfNumber=0
count=0
numbers=[random.randint(1,100) for _ in range(5)]
count=len(numbers)
TotalSum=sum(numbers)
print(TotalSum)
for num in numbers:
    TotalOfNumber+=num
    print(TotalOfNumber)
    print(count)
    
    
average= TotalOfNumber/count
print(f"Average of {count} numbers: {average:.2f}")   


