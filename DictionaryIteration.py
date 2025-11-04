try:
    Dictionary_List = {"Name": "John", "Age": 30, "City": "New York"}
    for key, value in Dictionary_List.items():
        print(f"{key}: {value}")
except Exception as e:
    print("An error occurred:", e)