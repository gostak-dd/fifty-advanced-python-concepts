class PayPalService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PayPal.")

class PaymentProcessor:
    def __init__(self):
        self.payment_service = PayPalService()

    def pay(self, amount):
        self.payment_service.process_payment(amount)

processor = PaymentProcessor()
processor.pay(100)

'''
Q: How does the code demonstrate tight coupling, and what are the potential drawbacks of this approach?
A: The code demonstrates tight coupling because the `PaymentProcessor` class is directly dependent on the 
`PayPalService` class. This means that if we want to change the payment service 
(for example, to use Stripe instead of PayPal), we would have to modify the 
`PaymentProcessor` class itself.
'''
