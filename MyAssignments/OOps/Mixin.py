class SaveMixin:
    def save(self):
        print(f"{self.__class__.__name__} saved to database")

class User(SaveMixin):
    def __init__(self, name):
        self.name = name

class Product(SaveMixin):
    def __init__(self, price):
        self.price = price

u = User("John")
u.save()
print(u)

p = Product(100)
p.save()
print(p)
