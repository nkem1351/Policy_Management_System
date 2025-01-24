class Payment:
    def __init__(self):
        self.payments = []

    def process_payment(self, policyholder, product):
        if policyholder.is_active and product.is_active:
            self.payments.append((policyholder.id, product.id, product.premium))
            print(f"Payment of {product.premium} processed for {policyholder.name} for product {product.name}")
        else:
            print(f"Payment failed: Check if policyholder and product are active.")

    def send_reminder(self, policyholder):
        print(f"Reminder sent to {policyholder.name} at {policyholder.email} for pending payment.")

    def impose_penalty(self, policyholder, amount):
        print(f"Penalty of {amount} imposed on {policyholder.name}.")
