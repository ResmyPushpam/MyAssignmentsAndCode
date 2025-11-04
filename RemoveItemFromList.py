ListOfItems = ['apple', 'banana', 'cherry', 'date']
itemToRemove = 'cherry'
if itemToRemove in ListOfItems:
    ListOfItems.remove(itemToRemove)
    print(f'{itemToRemove} has been removed from the list.')
else:
    print(f'{itemToRemove} is not in the list.')