class PayPalService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PayPal.")

class PaymentProcessor:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def pay(self, amount):
        self.payment_service.process_payment(amount)

# Inject dependency
payment_service = PayPalService()
processor = PaymentProcessor(payment_service)
processor.pay(100)

'''
Q: What is dependency injection, and how is it demonstrated in the provided code?
A: Dependency injection is a design pattern in which an object receives its dependencies from an 
external source rather than creating them itself. This promotes loose coupling and makes the code more
flexible and testable. In the provided code, the `PaymentProcessor` class depends on
    a payment service to process payments. Instead of creating an instance of `PayPalService` inside
    the `PaymentProcessor` class, the dependency is injected from outside.
'''
