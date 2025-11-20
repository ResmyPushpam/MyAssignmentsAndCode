'''Given two arrays of equal length, write a program that uses loops to create a third array where 
each element is the sum of the corresponding elements from the first two arrays. 
Example: [1, 2, 3] and [4, 5, 6] would produce [5, 7, 9]. '''
Array1=[1,2,3]
Array2=[4,5,6]
Array3=[]

for i,j in zip(Array1,Array2):
    Array3.append(i+j)
    
print(Array3)