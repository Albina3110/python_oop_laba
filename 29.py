class User:
    def setName(self, name):
        self.name = name 

    def getName(self):
        return self.name 


class Employee(User):
    pass
if __name__ == "__main__":
    employee = Employee()
    employee.setName('Clara Nous')
    name = employee.getName()
    print(name)  






