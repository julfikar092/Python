class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print(
            f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage {self.mileage}")


class Bus(Vehicle):
    pass


car = Bus("School Volvo", "250KM/H", "20KM/L")

car.display()
