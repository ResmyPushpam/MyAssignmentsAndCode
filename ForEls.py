try:
    items = ["apple", "banana", "cherry"]
    search_item = "banana"

    for item in items:
        if item == search_item:
            print(f"{search_item} found in the list.")
            break
    else:
        print(f"{search_item} not found in the list.")

except Exception as e:
    print("An error occurred:", e)