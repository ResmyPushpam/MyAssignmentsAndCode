'''Class method and static method
class level attributes and class level functions'''

class Order:
    total_orders = 0

    def __init__(self,orderid,amount):
        self.orderid=orderid
        self.amount = amount
        Order.total_orders +=1
    
    @classmethod
    def total_count_orders(cls):
        return 'Total Count is {}'.format(Order.total_orders)