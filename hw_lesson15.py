class Person:
    def __init__(
        self, 
        first_name:str, 
        last_name:str, 
        age:int,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):  
    def __init__(self, student_id, *args):
        super().__init__(*args)
        self.student_id = student_id

    def get_full_name_and_id(self):
        return f'{self.get_full_name()}, ID: {self.student_id}'

class Teacher(Person):
    def __init__(self, employee_id, *args):
        self.employee_id = employee_id
        super().__init__(*args)

    def teach(self):
        return f'Вчитель {self.first_name} надає урок у свої'\
      f'{self.age} років, його призвіще {self.last_name}'

class Employee(Person):
    def __init__(self,
                daily_salary: float,
                *args
                ):
        self.daily_salary = daily_salary
        super().__init__(*args)

    def work(self):
        return f'Here is {self.first_name}. I came to work'
    
class Recruiter(Employee):
    def __init__(self, *args):
        super().__init__(*args)
    def __str__(self):
        return f'{self.get_full_name} is a Recruiter'
    def work(self):
        return f'I come to the office and start to hiring.'

class Developer(Employee):
    def __init__(self, *args):
        super().__init__(*args)
    def __str__(self):
        return f'{self.get_full_name} is a Developer'
    def work(self):
        return f'I come to the office and start to coding.'


lena = Recruiter(15.50, 'Olena', 'Osipova', 26)
print(lena.work())
print(lena.str())


anatoliy = Person('Dima','Golova',18)
print(anatoliy.get_full_name())
sasha = Teacher('Sasha','Borisov',99,1)
print(sasha.teach())
print(sasha.get_full_name())
