from abc import abstractmethod, ABC

class PaymentProcessor(ABC):
    @abstractmethod 
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f'Processing {amount} via credit card')

class MobilePayment(PaymentProcessor):
    def pay(self, amount):
        print(f'Processing {amount} via mobile banking')

class NetBankingPayment(PaymentProcessor):
    def pay(self, amount):
        print(f'Processing {amount} via Net Banking')

def checkout(payment: PaymentProcessor, amount: float):
    payment.pay(amount)

# Instances of payment types
cc1 = CreditCardPayment()
nb1 = NetBankingPayment()
mb1 = MobilePayment()

# Processing payments
checkout(cc1, 500)  # Credit card payment
checkout(nb1, 300)  # Net banking payment
checkout(mb1, 150)  # Mobile payment
