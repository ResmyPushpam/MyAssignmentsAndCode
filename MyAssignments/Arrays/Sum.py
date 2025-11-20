'''Given two arrays of equal length, write a program that uses loops to create a third array where 
each element is the sum of the corresponding elements from the first two arrays. 
Example: [1, 2, 3] and [4, 5, 6] would produce [5, 7, 9]'''
array1=list(range(1,10))
array2=list(range(12,21))
array3=[]
for i in range(len(array1)):
    array3.append(array1[i] + array2[i])
print(f"Array1:{array1}")
print(f"Array2:{array2}")
print(f"Array3:{array3}")
