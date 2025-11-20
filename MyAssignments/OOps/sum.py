array1 = [1, 2, 3]
array2 = [4, 5, 6]
result = []

for i in range(len(array1)):
    sum_value = array1[i] + array2[i]
    result.append(sum_value)

print(result)