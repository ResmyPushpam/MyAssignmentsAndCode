class Order:
    total_order=0
    def __init__(self,order_id,amount):
        self.order_id=order_id
        self.amount=amount
        Order.total_order += 1

    @classmethod
    def totalorder(cls):
        print("f Total orders made{Order.total_order}")
o1 = Order(12,400)
o2 = Order(13,500)
print(o1.total_order)