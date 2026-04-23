class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def show_cart(self):
        total = sum(p.price for p in self.cart)
        for p in self.cart:
            print(p.name, p.price)
        print("Total:", total)

p1 = Product("Shoes", 1500)
c = Customer("Raj")
c.add_to_cart(p1)
c.show_cart()
