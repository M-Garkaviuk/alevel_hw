# S1 = 'Welcome to string'
# S2 = "Another string"
# S3 = """Another 
# big
# string!"""
# S4 = 'This "string" is a bit """crazy"""'

# S = 'abc'
# print(len(S))
# S = S + "12"
# print(S)
# print(S[2])
# print(S[1:3]*5)
# S = "adsfasddwwg"
# # S[7] = 4
# S = S[:5] + "5" + S[6:]
# print(S)

# S = "Welcome to California!"
# S[:5]
# S[5:]
# S[:]
# S[-3:]
# S[:-3]
# S[::3]
# S[::-1]
# S[:5:2]
# len(S)
# S.find("C")
# S.replace('C', '7')
# S.split()
# S.upper()
# S += '\n\n'
# S.strip()
# S = 'Welcome'
# R = 'Ukraine'
# K = S + ' to ' + R
# print('%s %s' % (S, R))
# C = "welcomed"
# S = "Ukraine"
# print("%d people are %s in %s" % (5, C, S))
# print("Hello %s!" % "Vasya")
# print('%d %s and %d %s' % (5, "peaches", 6, "bananas"))
# print('%(language)s has %(number)03d quite types' % {"language":"Python", "number":2})
# print('%.2s' % "Hello")
# print('%+10f' % 25)
# print('%+10s' % "Hello")
# var1 = 'Hello world1'
# var2 = 'Python programming!'
# print("var1[0]:", var1[0])
# print("var2[1:5]", var2[1:5])
# print("Updated string: ", var1[:6] + var2[:7])





# Hardcore
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# list_b = [x for x in list_a]
# list_b = [x for x in list_a if x % 2 == 0]
# list_b = [x for x in list_a if x % 2 == 0 and x > 0]
# list_b = [x*x for x in list_a]

# list_a = ['a', 'asd', 'asfet']
# list_b = [len(x) for x in list_a]

# list_b = [x if x < 0 else x**2 for x in list_a]
# list_b = [x**2 if x < 0 else x**3 for x in list_a if x % 2 == 0]

# print(list_b)

numbers = range(10)

squared_evens = [x**2 for x in numbers if x % 2 == 0 ]
squared_evens_1 = [
    n**2
    for n in numbers
    if n % 2 == 0
]
print(squared_evens, '''/n''', squared_evens_1)



