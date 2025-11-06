def merge_sorted_arrays(array1, array2):
    merged = []
    i = 0  # index for array1
    j = 0  # index for array2

    # Compare elements from both arrays and merge in sorted order
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1

    # Add remaining elements from array1
    while i < len(array1):
        merged.append(array1[i])
        i += 1

    # Add remaining elements from array2
    while j < len(array2):
        merged.append(array2[j])
        j += 1

    print("Merged array:", merged)
    return merged

# Example usage:
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
merge_sorted_arrays(array1, array2)