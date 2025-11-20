'''static method
not to use self,cls
we ar e not trying to access both class level data and object level data'
then we go for static method'''

class Order:
    
    @staticmethod
    def apply_discount(amount,dt_percntage):
        return amount-(amount*dt_percentage/100)

dt_calc = Order.apply_discount(1000,10)
print(dt_calc)
