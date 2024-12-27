class User:
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
class Employee(User):
    def __init__(self, name, salary):
        super().__init__(name) 
        self.__salary = salary

    def getSalary(self):
        return self.__salary
if __name__ == "__main__":
    employee = Employee('Clara', 50000)
    print(f"Имя: {employee.getName()}, Зарплата: {employee.getSalary()}")





