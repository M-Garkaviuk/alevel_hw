# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
# filename = 'Lesson_3_Numbers.txt'
# with open(filename, 'r') as f:
#     for line in f:
#         line = line.strip()
#         numbers = list(map(int, line.split()))
#         fizz = numbers[0]
#         buzz = numbers[1]
#         n = numbers[2]

#         result_list = []
#         shag = range(1, n+1)
#         for i in shag:
#             if i % fizz == 0 and i % buzz == 0:
#                 result_list.append('FB')
#             elif i % fizz == 0:
#                 result_list.append('F')
#             elif i % buzz == 0:
#                 result_list.append('B')
#             else: result_list.append(str(i))
#             print(result_list)    
# f.close()



filename = 'Lesson_3_Numbers.txt'
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        numbers = list(map(int, line.split()))
        fizz = numbers[0]
        buzz = numbers[1]
        n = numbers[2]

        result_list = []
        shag = range(1, n+1)
        for i in shag:
            if i % fizz == 0 and i % buzz == 0:
                result_list.append('FB')
            elif i % fizz == 0:
                result_list.append('F')
            elif i % buzz == 0:
                result_list.append('B')
            else: result_list.append(str(i))
            print(result_list)  
f.close()
with open ('new.txt', 'w') as file:
    file.write(str(result_list))
file.close()
