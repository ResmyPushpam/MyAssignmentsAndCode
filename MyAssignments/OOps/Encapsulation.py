class Student:
    def __init__(self,name,marks):
        self.__name= name
        self.__marks= marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if (0<= marks <= 100):
            self.__marks=marks
        else:
            print(f"{marks}")

std =Student("Roy",34)
print(std.get_marks())
std.set_marks(95)
print(std.get_marks())
print(std.__marks)
