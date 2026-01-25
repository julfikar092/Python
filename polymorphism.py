class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel(self):
        return "Petrol or Diesel"

class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel(self):
        return "Electric Charge"

my_electric_car = Electric_Car("Tesla", "Safari", "85kWh")
print(my_electric_car.fuel())

my_normal_car = Car("Toyota", "Corolla")
print(my_normal_car.fuel())