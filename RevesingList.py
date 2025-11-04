List = [1, 2, 3, 4, 5]
ReversedList = []
for i in range(len(List)-1, -1, -1):
    ReversedList.append(List[i])
print("Reversed List:", ReversedList)   