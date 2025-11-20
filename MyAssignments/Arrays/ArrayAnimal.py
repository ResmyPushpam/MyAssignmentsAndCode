'''write a program that takes an array of words ["cat", "dog", "elephant", "ant", "bear"] and uses a 
loop to display only the words that have more than 3 letters.'''
ArrayWords=["cat", "dog", "elephant", "ant", "bear"]
for animal in ArrayWords:
    if len(animal)>3:
        print(animal)


