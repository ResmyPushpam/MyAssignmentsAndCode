'''Given an array of test scores [67, 82, 91, 74, 88], write a program that uses a loop to count how 
many scores are above 70. '''
test_scores= [67,82,91,74,88]
count=0
for score in test_scores:
 if score >70:
   count+=1
print(count)
