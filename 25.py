class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary
class EmployeesCollection:
    def __init__(self):
        self.__employees = []

    def add(self, employee):
        self.__employees.append(employee)

    def show(self):
        for employee in self.__employees:
            print(f"Имя: {employee.getName()}, Зарплата: {employee.getSalary()}")

    def total_salary(self):
        total = sum(employee.getSalary() for employee in self.__employees)
        return total

    def average_salary(self):
        if len(self.__employees) == 0:
            return 0  # Избегаем деления на ноль
        total = self.total_salary()
        return total / len(self.__employees)
if __name__ == "__main__":
    ec = EmployeesCollection()
    ec.add(Employee('Clara Nous', 50000))
    ec.add(Employee('Caleb Vatore', 60000))
    ec.add(Employee('Lilit Novoselskikh', 55000))
    ec.show()
    total = ec.total_salary()
    print(f"Суммарная зарплата всех работников: {total}")
    average = ec.average_salary()
    print(f"Средняя зарплата работников: {average}")





