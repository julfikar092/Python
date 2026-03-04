class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


b = Bus("Volvo", "250Klh", "20M/L")

print(b.seating_capacity())


""" print(f"Vehicle Name: {b.name} \nSpeed: {b.max_speed} \nMileage: {b.mileage}") """
