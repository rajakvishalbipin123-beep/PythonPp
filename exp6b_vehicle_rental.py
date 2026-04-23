class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.available = True

    def book(self, days):
        if self.available:
            self.available = False
            print("Cost:", self.price * days)
        else:
            print("Not available")

    def return_vehicle(self):
        self.available = True

car = Vehicle("Car", 1000)
car.book(2)
car.return_vehicle()
