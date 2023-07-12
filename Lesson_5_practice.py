# def function_1():
#     return "Hello!"

# print(function_1())

# def function_2(num1, num2):
#     result = num1 + num2
#     return result
# ten = 10
# five = 5
# print(function_2(ten, five))

# test_var = "Global value"

# def test_global():
#     print(f'"test_global" has: {test_var}\n')
# def test_local():
#     test_var = "Local value"
#     print(f'"test_local" has: {test_var}\n')
# def change_global():
#     global test_var
#     test_var += " and local value"
#     print(f'"change_global" has: {test_var}\n')

# print(f'Global varaible equals to: {test_var}')
# test_global()
# print(f'"Global variable" equals to: {test_var} ')
# test_local()
# print(f'"Global variable" equals to: {test_var} ')
# change_global()
# print(f'"Global variable" equals to: {test_var} ')

# def test(a, b=10, *c, **d):
#     summa = a + b
#     if c:
#         summa += sum(c)
#     if d:
#         summa += sum(d.values())
#     return summa
# print(test(15))
# print(test(15,5)) 
# print(test(15, 5, 1, 2, 3))
# print(test(15, 5, 1, 2, 3, x=10, y=20))

# def run_operation(num1, num2, operation):
#     return operation(num1, num2)
# def plus(num1, num2):
#     return num1, num2
# minus = lambda num1, num2: num1 - num2

# print(run_operation(10, 5, plus))
# print(run_operation(10, 5, minus))

# # lamda arguments: expression
# lambda age: "Senior" if age > 55 else "Adult"
# (lambda x, y: x+y)(2, 3) 

# def my_squre(num):
#     return num**2
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_numbers = list(map(my_squre, numbers))
# print(squared_numbers)

filter(lambda x: x%2, range(10))
print(list(filter(lambda x: x%2, range(10))))

from functools import reduce
reduce(lambda x, y: x+y, range(10))
