import math
class Shape:
    def __init__(self):
        print(f"{self.__class__.__name__} object created")

    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")

        
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.__radius = radius
    def area(self):
        return math.pi*(self.__radius**2)
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__()
        self.width = width
        self.height= height
    def area(self):
        return self.width*self.height

def calculate_total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

circle = Circle(5)
rectangle = Rectangle(20,30)
print("CircleArea",circle.area())



shapes = [Circle(3),Rectangle(2,8),Circle(7)]

print("Total area of Shapes",calculate_total_area(shapes))




    

    
