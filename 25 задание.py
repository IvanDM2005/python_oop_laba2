class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeesCollection:

    def __init__(self):
        self.__employees = []

    def add(self, employee):
        self.__employees.append(employee)

    def show(self):
        for employee in self.__employees:
            print(employee.name)

    def total_salary(self):
        total = 0
        for employee in self.__employees:
            total += employee.salary
        return total

collection = EmployeesCollection()

collection.add(Employee("Иван", 50000))
collection.add(Employee("Петр", 60000))

collection.show()
print(collection.total_salary())