class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


b = Bus("Volvo", "250Klh", "20M/L")

print(f"Vehicle Name: {b.name} \nSpeed: {b.max_speed} \nMileage: {b.mileage}")
