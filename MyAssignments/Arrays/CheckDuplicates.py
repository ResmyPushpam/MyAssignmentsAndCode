'''Question 17 
Given an array of numbers, write a program that uses nested loops to check if there are any 
duplicate values in the array. Display "Duplicates found" or "No duplicates" accordingly. '''
from pathlib import Path
Array=[23,45,56,67,78,67,45,23]
duplicateArray=[]
found_duplicates=False
for i in range(len(Array)):
    for j in range(i+1,len(Array)):
        if Array[i]==Array[j]:
            found_duplicates=True
            break
        if found_duplicates:
            break
result = "Duplicates found" if found_duplicates else "No duplicates"
print(result)
p = Path(__file__).parent/'data'/'DuplicateCheck.txt'
try:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(result, encoding='utf-8')
    print(f"Result saved to: {p}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}") 

         
