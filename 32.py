class User:
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('Возраст должен быть больше 0')

class Employee(User):
    def setAge(self, age):
        if age <= 120:
            super().setAge(age) 
        else:
            raise Exception('Возраст должен быть меньше 120')

# Пример использования
if __name__ == "__main__":
    employee = Employee()
    
    try:
        employee.setAge(30)  
        print(f"Возраст установлен: {employee.age}")
        
        employee.setAge(150) 
    except Exception as e:
        print(e)

    try:
        employee.setAge(-5)  
    except Exception as e:
        print(e)







