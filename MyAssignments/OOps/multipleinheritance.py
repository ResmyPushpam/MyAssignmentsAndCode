class Calc1:
    def addition(self, a,b):
        return a + b
class Calc2:
    def multiply(self,a,b):
        return a * b
class Calc3(Calc1, Calc2):
    def subtract(self,a,b):
        return a-b
c= Calc3()
print(c.addition(3,5))
print(c.multiply(6,7))
print(c.subtract(9,8))

print(Calc3.__mro__)
