class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("The full name of the car is: ", self.brand, self.model)

Private_Car = Car("Toyota", "Scorpion")

print(Private_Car.brand)
print(Private_Car.model)

my_new_car = Car("Tata","Safari" )
print(my_new_car.model)

my_new_car.display_info()

# Inheritance
class Electric_Car(Car):
    def __init__(self,brand, model, BatterySize):
        super().__init__(brand,model)
        self.BatterySize = BatterySize

my_new_Electric_car = Electric_Car("Tesla", "Model S", "85kWh")
my_new_Electric_car.display_info()

print(f"{my_new_Electric_car.brand} {my_new_Electric_car.model}; Batter size : {my_new_Electric_car.BatterySize}")