class Policyholder:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = True
        self.products = []

    def register_product(self, product):
        if self.is_active:
            self.products.append(product)
            print(f"{self.name} has registered for product: {product.name}")
        else:
            print(f"Policyholder {self.name} is suspended. Reactivate before registering products.")

    def suspend(self):
        self.is_active = False
        print(f"{self.name} has been suspended.")

    def reactivate(self):
        self.is_active = True
        print(f"{self.name} has been reactivated.")
