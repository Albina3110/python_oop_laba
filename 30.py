class User:
    def setName(self, name):
        self.name = name 

    def getName(self):
        return self.name 


class Employee(User):
    def __init__(self):
        self.salary = None
        self.surname = None
    def setSalary(self, salary):
        self.salary = salary 

    def getSalary(self):
        return self.salary 
    def setSurname(self, surname):
        self.surname = surname 

    def getSurname(self):
        return self.surname 
if __name__ == "__main__":
    employee = Employee()
    employee.setName('Clara')
    employee.setSurname('Nous')
    employee.setSalary(50000)
    name = employee.getName()
    surname = employee.getSurname()
    salary = employee.getSalary()

    print(f"Имя: {name}, Фамилия: {surname}, Зарплата: {salary}")








