class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary
employees = [
    Employee('Clara Nous', 50000),
    Employee('Alise Kit', 60000),
    Employee('Caleb Vatore', 55000),
]
for employee in employees:
    print(f"Имя: {employee.getName()}, Зарплата: {employee.getSalary()}")




