# i = res = 0
# while i < 11:
#     res += i
#     i += 1
# print(res)

# i = 10
# while True:
#     i -= 1
#     if not i: continue
#     if i%2:
#         print(i)
#     if i < -11: break

# # 
# sum_1 = []
# for i in 'word':
#     sum_1 += i
# print (sum_1)

# a = [10, 20, 30, 40, 50]
# for id, item in enumerate(a):
#     a[id] = item + 5
# print(a)

# import sys
# filename = sys.argv[0]
# f = open('filename', 'r')
# # f.write ("hello")
# for line in f:
#     print(line)
# f.close()

# with open('E:\Education\GoIT\Game\Lesson_3_Numbers.txt', 'w') as f:
#     f.write("Hello")
# f.close()

# програма виводить сама себе:
# with open('Lesson_3_practice.py', 'r') as f: 
    
#     for line in f:
#         print(line)
# f.close()

# програма виводить сама себе задом наперед
# with open('E:\Education\GoIT\Game\Lesson_3_practice.py', 'r') as f:
#     for text in reversed(f.readlines()):
#         print(text)
# f.close()

# Банкомат видає суму максимально можливими купюрами:
# ammount = int(input("Введіть сумму кратну 10 грн: "))
# nominals = [10, 20, 50, 100, 200, 500, 1000]
# output = {}
# for item in nominals[::-1]:
#     while ammount > 0:
#         if ammount >= item:
#             if item in output:
#                 output[item] += 1
#             else:
#                 output[item] = 1
#             ammount -= item
#         else: break
# print(output)

# Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
ammount = int(input("Введіть сумму кратну 10: "))
nominals = [10, 20, 50, 100, 200, 500, 1000]

output = []

for item in nominals:
    # while ammount > 0:
        if ammount - item % 20 != 0:
            print(ammount - item % 20)