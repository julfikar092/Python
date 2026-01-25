class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    
    def display_info(self):
        print("The full name of the car is: ", self.__brand, self.model)

My_Car = Car("Toyota","Corolla")

print(My_Car.get_brand())

