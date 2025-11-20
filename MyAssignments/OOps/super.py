class Parent:
    def __init__(self):
        print("parent init")
class child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")

c=child()

print(child.__mro__)