ListOfNumber = [1,2,4,5,2,6,7,8,2,9,2]
itemToCount =2
count = 0
for number in ListOfNumber:
    if number == itemToCount:
        count +=1
print(f"The item {itemToCount} occurs {count} times in the list.")
