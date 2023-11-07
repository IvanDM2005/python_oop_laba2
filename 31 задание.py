class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.age = None

    def setAge(self, age):
        if age >= 18 and age <= 65:
            self.age = age
        else:
            raise Exception("Invalid age")

    def getAge(self):
        return self.age