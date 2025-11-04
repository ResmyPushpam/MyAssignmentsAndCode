numbers=[3,56,3,9,3,4,3,6,3,8,3]
count=0
target=3
for num in numbers:
    if num ==target:
        count+=1
print(f"The number {target} occurs {count} times in the list.")