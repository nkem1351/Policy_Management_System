class Product:
    def __init__(self, id, name, premium):
        self.id = id
        self.name = name
        self.premium = premium
        self.is_active = True

    def update_premium(self, new_premium):
        self.premium = new_premium
        print(f"Product {self.name} premium updated to {new_premium}")

    def suspend(self):
        self.is_active = False
        print(f"Product {self.name} has been suspended.")
