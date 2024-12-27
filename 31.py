class User:
    def setName(self, name):
        self.name = name 

    def getName(self):
        return self.name 


class Employee(User):
    def __init__(self):
        self.salary = None
        self.surname = None
        self.age = None  
    def setSalary(self, salary):
        self.salary = salary 

    def getSalary(self):
        return self.salary 
    def setSurname(self, surname):
        self.surname = surname 

    def getSurname(self):
        return self.surname 
    def setAge(self, age):
        if 18 <= age <= 65:
            self.age = age
        else:
            raise Exception("Возраст должен быть в диапазоне от 18 до 65 лет.")

    def getAge(self):
        return self.age 
if __name__ == "__main__":
    employee = Employee()
    employee.setName('Clara ')
    employee.setSurname('Nous')
    employee.setSalary(50000)
    try:
        employee.setAge(30) 
        print(f"Возраст установлен: {employee.getAge()}")
        
        employee.setAge(70)  
    except Exception as e:
        print(e)
    name = employee.getName()
    surname = employee.getSurname()
    salary = employee.getSalary()

    print(f"Имя: {name}, Фамилия: {surname}, Зарплата: {salary}")







