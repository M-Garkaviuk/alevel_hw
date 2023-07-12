# Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до нижнього регістру. Друга функція прийматиме рядок та приводитиме його до верхнього регістру.

# Головна програма має застосовувати обидві функції до списку рядків за допомогою map, для кожного з рядків, та друкувати результат.
# l = "rfHYbdvdHBONpjv"
# str_list = list(l)

# def operation1(str):
#     return [x.lower() for x in str] 

# def operation2(str):
#     return [y.upper() for y in str]

# def main(str, lower, upper):
#     result = list(map(lambda x, y: x + ' ' + y, lower(str), upper(str)))
    
#     for item in result:
#         print(item) 

# main(str_list, operation1, operation2)

# Написати функцію, яка буде підносити число у квадрат. 
# Написати другу, яка буде перевіряти, чи є число простим.
#  Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку 
# від 0 до 50 за допомогою map


# def square_number(number):
#     return number ** 2

# def is_simple(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# numbers = range(51)
# simples = filter(is_simple, numbers)
# squared_simples = map(square_number, simples)

# for number in squared_simples:
#     print(number)

# Візьміть файл, в якому є багато англійських слів у рядках. 
# Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.

# def count_word_frequency(filename):
#     word_frequency = {}

#     # Відкриваємо файл для читання
#     with open(filename, 'r') as file:
#         # Проходимося по кожному рядку у файлі
#         for line in file:
#             # Розділяємо рядок на окремі слова
#             words = line.strip().split()
            
#             # Проходимося по кожному слову
#             for word in words:
#                 # Оновлюємо лічильник для даного слова
#                 word_frequency[word] = word_frequency.get(word, 0) + 1
    
#     return word_frequency

# def print_word_frequency(word_frequency):
#     # Сортуємо словник за значеннями (кількістю зустрічей)
#     sorted_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

#     # Виводимо слова та їх кількшість
#     for word, count in sorted_frequency:
#         print(f'{word}: {count}')

# filename = 'Readme.txt' 
# word_frequency = count_word_frequency(filename)

# print_word_frequency(word_frequency)

# Пробуємо написати свій власний zip.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

def my_zip(list1, list2):
    new_list_counter = len(list1)
    new_list = []
    while new_list_counter > 0:
        new_list.append(str(list1[0]) + str(list2[0]))
        list1.pop(0)
        list2.pop(0)
        new_list_counter -= 1
    return new_list 
print(my_zip(list1, list2))
