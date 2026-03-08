class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = float(salary)

    def update_salary(self, new_salary):
        self.salary = float(new_salary)


employees = {}

with open("Innovative Skills/Exam - 1/test8.txt") as file:
    content = file.readlines()

    total_employees = int(content[0].strip())

    for i in range(1, total_employees + 1):
        employee_data = content[i].strip().split()
        emp_id = employee_data[0]
        name = employee_data[1]
        salary = employee_data[2]

        employees[emp_id] = Employee(emp_id, name, salary)

    all_employees = list(employees.values())

    highest_paid_employee = all_employees[0]

    for person in all_employees:
        if person.salary > highest_paid_employee.salary:
            highest_paid_employee = person

    print(f"Highest Salary Employee: {highest_paid_employee.name}")
    print(f"Salary: {highest_paid_employee.salary:.2f}")
