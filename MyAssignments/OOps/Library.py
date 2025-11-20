class Item:
    def __init__(self,title):
        self.__title=title
        self.__is_borrowed = False
    
    def get_title(self):
        return self.__title
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed=True
            print(f"{self.__title} has been borrowed")
        else:
            print(f"{self.__title} is already borrowed")
    def return_item(self):
                if self.__is_borrowed:
                    self.__is_borrowed = False
                    print(f"{self.__title} has been returned.")
                else:
                    print(f"{self._title } was not borrowed")
    def is_borrowed(self):
                        return self.__is_borrowed
class Book(Item):
    def __init__(self, title,author):
        super().__init__(title) 
        self.__author= author

    def get_info(self):
        return f"Book: {self.get_title} | Author: {self.__author}"

class Magazine(Item):
    def __init__(self, title ,issue_number):
        super().__init__(title)
        self.__issue_number = issue_number
    def get_info(self):
        return f"Book: {self.get_title} | Issue: {self.__issue_number}"

class Library:
    def __init__(self):
        self.__items = []
    def add_item(self,item):
        self.__items.append(item)
        print(f"Added: {item.get_title()}")
        
    def list_items(self):
        print("\n=== Library Items ===")
        for item in self.__items:
            status = "Borrowed" if item.is_borrowed() else "Available"
            print(f"{item.get_info()} | Status: {status}")
        print("============================\n")
    def find_item(self,title):
            for item in self.__items:
                if item.get_title().lower():
                    return item
            print("item not found")
            return None


            if item.get_title().lower() == title.lower():
                return item
            print("item not found")
            return None 
    

library = Library()
library.add_item(Book("SQL","Max"))
library.add_item(Book("HTML","Jordan"))
library.add_item(Magazine("science weekly",42))
library.list_items()
item = library.find_item("SQL")
if item:
    item.borrow()
    item.borrow()
    item.return_item()
    library.list_items()
        
    
    
    
