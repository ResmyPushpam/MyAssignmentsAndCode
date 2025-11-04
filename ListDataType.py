try:
    # Use a LIST, not a set
    List_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Max_number = List_number[0]  # Initialize outside loop

    for num in List_number:
        if num > Max_number:
            Max_number = num  # Update only if larger

    print(f"The largest number in the list is: {Max_number}")
    print("End of List")

except Exception as e:
    print("An error occurred:", e)