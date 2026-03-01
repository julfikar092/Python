# Task 1: University Course System

""" class Course:
    def __init__(self, course_name, credit, instructor):
        self.course_name = course_name
        self.credit = credit
        self.instructor = instructor

    def display_info(self):
        print(
            f"This '{self.credit}' credit '{self.course_name}' course is taken by '{self.instructor}'")


Course1 = Course("C", 3, "Kazi Shakib")
Course2 = Course("Java", 3, "Alim")

Course1.display_info()
Course2.display_info() """

""" Output:

This '3' credit 'C' course is taken by 'Kazi Shakib'
This '3' credit 'Java' course is taken by 'Alim'

"""


# Task 2: Design a class CoffeeMachine that:

""" class CoffeeMachine:
    def __init__(self, brand_name):
        self.brand_name = brand_name
        self.__water_ = 5

    def add_water(self, amount):
        self.__water_ += amount

    def make_coffee(self):
        self.__water_ -= 0.25

    def check_water(self):
        return self.__water_


CM1 = CoffeeMachine("Philips")

CM1.add_water(2)
CM1.make_coffee()
water_level = CM1.check_water()

print(
    f"Current water level after adding 2 liter water and make 1 Coffee: {water_level}") """

"""
Output:
Current water level after adding 2 liter water and make 1 Coffee: 6.75

"""


# Task 3: Hospital Record System (Encapsulation + Inheritance)

""" class Person:
    def __init__(self, name, national_id):
        self.name = name
        self.__national_id = national_id

    def get_nid_info(self):
        return self.__national_id


class Patient(Person):
    def __init__(self, name, national_id):
        super().__init__(name, national_id)
        self.__medical_history = {}

    def add_record(self, key, value):
        self.__medical_history[key] = value

    def view_medical_history(self):
        return self.__medical_history


P1 = Patient("Julfikar", "5847684669")

P1.add_record("Date ", "12 July, 2025")
P1.add_record("Weight ", "72")
P1.add_record("Blood Pressure ", "115/85")


print(f"Patient Name: {P1.name}")
print(f"National ID:  {P1.get_nid_info()}")
print("-" * 30)
history = P1.view_medical_history()

print("Medical History:")
for key, value in history.items():
    print(f"{key}: {value}")

 """
# Task 4: Company Payroll System


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Error: Salary must be positive.")
            self.__salary = 0

    def get_salary(self):
        return self.__salary

    def display_info(self):
        print(f"Name : {self.name}\nSalary: {self.get_salary()}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.__department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.__department}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.__programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Language: {self.__programming_language}")


M = Manager("Sultan Ahmed", 5000, "IT")
D = Developer("Nafis Sadik", 6000, "Python")

M.display_info()
D.display_info()

""" 
Output:

Name : Sultan Ahmed
Salary: 5000
Department: IT
Name : Nafis Sadik
Salary: 6000
Language: Python 

"""

print("\nSet negative salary: ")
M.set_salary(-500)
M.display_info()

""" 
Output:

Set negative salary:
Error: Salary must be positive.
Name : Sultan Ahmed
Salary: 0
Department: IT

 """

# Attempt illegal direct access and show restriction

print(M.__salary)
# AttributeError: 'Manager' object has no attribute '__salary'. Did you mean: 'get_salary'?

print(M.__department)
# AttributeError: 'Manager' object has no attribute '__salary'. Did you mean: 'get_salary'?
