class Student:
    pass
class Employee:
    pass
employee = Employee()
print(isinstance(employee, Employee))  
print(isinstance(employee, Student))    
class Student:
    name = None
    def __init__(self, name):
        self.name = name
class Employee:
    name = None
    def __init__(self, name):
        self.name = name
users = [
    Student('Клара Ноус'),
    Employee('Френсис Галлагер'),
    Student('Лилит Новосельских'),
    Employee('Калеб Ваторе'),
    Student('Себастьян Швагенвагенс '),
    Employee('Роузи Кит'),
    Student('Лала Кроуз'),
]
for user in users:
    if isinstance(user, Employee):
        print(user.name)

