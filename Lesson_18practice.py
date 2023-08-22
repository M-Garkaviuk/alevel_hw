# class Car:
#     def __init__(self, name: str):
#         self.name = name
#         print('created: ', self.name)
#
#     def __str__(self):
#         return f'Car: {self.name}'
#
#
# car = Car('name')
# car_2 = Car('')
#
# print(car)
#
# # car_1 = Car('car_1')
# # car = Car('car')
# # new_car = Car
# # Car = Car('Car')
# #
# # car_2_ = new_car('new_car_2')
# #
# # def func(s:str) -> None:
# #     print(s)
# #
# # my_f = func
# #
# # func('Hello')
# #
# # print(func)
# # print('my_f')
# # del func
# # my_f('my_f 2')
# # func('Hello')
#
# def dec(func):
#     def wrap():
#         res = func()
#         return res
#     return wrap
#
# a = 2
# s = 's'
#
# built-in
# global
# local
# nonlocal
#
#
# def dec(func):
#     print ('decorator in ')
#     def wrapper():
#         print('wrapper in')
#         res = func()
#         print ('wrapper out')
#         return res
#     print('decorator out')
#     return wrapper
#
#
# @dec
# def b():
#     print('func b')
#     return "Hi, I am B"
#
# @dec
# def a():
#     print('func a')
#     return "Hi. I am A"
#
# decorated = dec(a)
#
# res = decorated()
# print(a())
#
# b()


