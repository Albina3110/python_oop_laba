class Position:
    def __init__(self, title):
        self.title = title

class Department:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department
position = Position('Software Engineer')
department = Department('Development')
user = User('Clara Nous', position, department)
print("Имя:", user.name)
print("Должность:", user.position.title)
print("Отдел:", user.department.name)




