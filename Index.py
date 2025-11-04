my_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
try:
    print(my_List[20])
except IndexError:
    print("Error: Index out of range.") 