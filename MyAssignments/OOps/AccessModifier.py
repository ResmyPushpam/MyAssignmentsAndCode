class Order:
    def __init__(self,order_id,amount):
        self.__order_id = order_id
        self.__amount = amount                   #private
 
    def get_amount(self):
        return self.__amount
   
    def __set_amount(self,amount):
        if amount >= 0:
            self.__amount = amount
        else:
            print('Invalid amount')
 
order = Order(15,500)
print(order.get_amount())
 
print(order.__set_amount(800))
print(order.get_amount())
 
print(order.__amount)