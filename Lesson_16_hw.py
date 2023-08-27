import datetime
import calendar


class Employee:
    def __init__(self, full_name: str, daily_salary: float):
        self.full_name = full_name
        self.daily_salary = daily_salary

    def __gt__(self, other):
        return self.daily_salary > other.daily_salary

    def __lt__(self, other):
        return self.daily_salary < other.daily_salary

    def __eq__(self, other):
        return self.daily_salary == other.daily_salary

    def __ne__(self, other):
        return self.daily_salary != other.daily_salary

    def work(self, hours_worked: float):
        return f'Here is {self.full_name}. I came to work'

    def calculate_monthly_salary(self, work_days: int):
        return self.daily_salary * work_days

    def check_salary(self, days: int):
        expected_salary = self.calculate_monthly_salary(days)
        return f'Expected salary: ${expected_salary:.2f}'


class Recruiter(Employee):
    def __str__(self):
        return f'{self.full_name} is a Recruiter'

    def work(self, hours_worked: float):
        return f'I come to the office and start to hiring.'


class Developer(Employee):
    def __init__(self, tech_stack: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tech_stack = tech_stack

    def __str__(self):
        return f'{self.full_name} is a Developer'

    def work(self, hours_worked: float):
        return f'I come to the office and start to coding.'

    def compare_number_of_tech(self, other_developer):
        self_tech_count = len(self.tech_stack)
        other_tech_count = len(other_developer.tech_stack)

        if self_tech_count > other_tech_count:
            return f'{self.full_name} knows more technologies than {other_developer.full_name}'
        elif self_tech_count < other_tech_count:
            return f'{other_developer.full_name} knows more technologies than {self.full_name}'
        else:
            return f'Both developers know the same number of technologies'

    def __add__(self, other_developer):
        new_name = f'{self.full_name} {other_developer.full_name}'
        new_tech_stack = list(set(self.tech_stack + other_developer.tech_stack))
        new_salary = max(self.daily_salary, other_developer.daily_salary)

        return Developer(tech_stack=new_tech_stack, full_name=new_name, daily_salary=new_salary)

def get_work_days_in_month(year, month):
    _, days_in_month = calendar.monthrange(year, month)
    work_days = 0
    for day in range(1, days_in_month + 1):
        current_date = datetime.date(year, month, day)
        if current_date.weekday() < 5:  # Check if a weekday(Mon-Fri)
            work_days += 1
    return work_days


lena = Recruiter('Olena Osipova', 15.50)

current_date = datetime.date.today()
work_days_this_month = get_work_days_in_month(current_date.year, current_date.month)


print(f'{lena.full_name} earned {lena.check_salary(work_days_this_month)} this month.')

john = Developer(['Python', 'JavaScript', 'React'], 'John Smith', 20.0)

peter = Developer(
    ['Java', "C++", 'SQL', 'Python', 'Ruby'],
    'Peter Jonson',
    25.0,
    )

print(john.tech_stack)
new_developer = john + peter
print( new_developer.full_name, new_developer.tech_stack, new_developer.daily_salary)
