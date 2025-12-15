class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): {self.price} PLN"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, category='{self.category}')"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.category == other.category
        return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    def __len__(self):
        return len(self.name)
