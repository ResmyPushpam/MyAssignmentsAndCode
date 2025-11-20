class Car:
    def __init__(self,brand):
        self._brand= brand
    def show(self):
        print("Brand",self._brand)

car= Car("BMW")
car.show()
print(car._brand)
