'''Write a function calculate_area(width, height)
 that takes two numbers and returns the area of a 
 rectangle.'''
try:
    def calculate_area(width, height):
        return(width*height)
    print(calculate_area(2,3))
except Exception as e:
    print("Error:",e)