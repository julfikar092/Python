class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    color = "White"


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


b = Bus("Volvo", "100Klh", "20M/L")
c = Car("Totoyota", "180Klh", "30M/L")

print(
    f"Color: {b.color}, Vehicle name: {b.name}, Speed: {b.max_speed}, Mileage: {b.mileage}")
print(
    f"Color: {c.color}, Vehicle name: {c.name}, Speed: {c.max_speed}, Mileage: {c.mileage}")
