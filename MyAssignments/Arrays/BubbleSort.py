'''Question 14 
Write a program that takes an array of numbers [34, 12, 67, 23, 89, 45] and uses a loop to sort 
them in ascending order using the bubble sort algorithm. '''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Reset swapped flag for each pass
        for j in range(0, n - i - 1):  # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:  # If no swaps, array is sorted
            break
    return arr

# Define the array from the question
array = [34, 12, 67, 23, 89, 45]
print(f"Original array: {array}")
sorted_array = bubble_sort(array)
print(f"Sorted array: {sorted_array}")