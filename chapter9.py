# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Started..")

#     @staticmethod
#     def stop():
#         print("Stopped..")


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name


# C1 = ToyotaCar("Curius", "Electric")
# C1.start()


class Circle:
    def __init__(self, radius):
        self.raius = radius

    def Area(self):
        return 3.1416 * (self.raius) ** 2

    def Perimeter(self):
        return 2 * 3.1416 * self.raius


c = Circle(5)
print(c.Area())
print(c.Perimeter())
