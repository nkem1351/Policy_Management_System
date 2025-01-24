from policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
ph1 = Policyholder(1, "Alice Johnson", "alice@example.com")
ph2 = Policyholder(2, "Bob Smith", "bob@example.com")

# Create products
prod1 = Product(101, "Life Insurance", 500)
prod2 = Product(102, "Health Insurance", 300)

# Create payment manager
payment_manager = Payment()

# Register products and process payments
ph1.register_product(prod1)
payment_manager.process_payment(ph1, prod1)

ph2.register_product(prod2)
payment_manager.process_payment(ph2, prod2)

# Suspend and reactivate policyholder
ph1.suspend()
ph1.reactivate()

# Display account details
print("\nPolicyholder Details:")
for ph in [ph1, ph2]:
    print(f"ID: {ph.id}, Name: {ph.name}, Active: {ph.is_active}, Products: {[p.name for p in ph.products]}")
