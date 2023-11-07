class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

employees = [
Employee("Иван", 50000),
Employee("Петр", 60000),
Employee("Сидор", 40000)
]

for employee in employees:
    print(employee.get_name())
    print(employee.get_salary())
    print()