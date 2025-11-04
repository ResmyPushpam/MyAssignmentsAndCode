ListofItems = ['apple', 'banana', 'cherry', 'apple', 'date', 'banana']
duplicates = set()
seen = set()
for item in ListofItems:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print("Duplicate items found:", duplicates)