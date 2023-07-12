# t = (2, 2.05, "Hello")
# (a, b, c) = t
# print(a, b, c)
# x = 12,
# tup = 1, 2, 'qwerty'
# tup = tup + (1, 2)
# print(tup)

# # Dictionaries
# d = {}
# d1 = {'a'}
# d = dict(short='dict', long='dictionary')
# d
# d = dict.fromkeys(['a', 'b', 1, (1, 2)])
# d = dict(a=15, b=45) 
# print(d['a'])
# print(d.get('e'))

# grades = dict(Ivanov = [10, 8, 11, 12, 8], Petrov = [8, 6, 10, 11], Sidorov = [5, 6, 7, 2])

# marks = []
# best_stud_name = ''  
# best_stud_av = 0
# worst_stud_name = ''
# worst_stud_av = 100


# for i in grades.values():
#     marks.extend(i)
# average = sum(marks) / len(marks)

# for key, value in grades.items():
#      average_grade = sum(value) / len(value)
#      if average_grade > best_stud_av:
#          best_stud_name = key
#          best_stud_av = average_grade   
#      if average_grade < worst_stud_av:
#          worst_stud_name = key
#          worst_stud_av = average_grade   
# print(average, best_stud_name, best_stud_av, worst_stud_name, worst_stud_av)




# # students = (Ivanov=[Python], Petrov=[FrontEnd], Sidorov=[FullStack], Savelyev=[Java], )    
# stud = dict([
#     ('FrontEnd',set(("Vasya", 'Kolya', 'Maryna'))),
#     ('Python',set(("Oleksa", 'Marjan', 'Maryna'))),
#     ('Java',set(("Nadia", 'Natalia', 'Vasya'))),
#     ('FullStack',set(("Vanessa", 'John', 'Ariel')))
# ])

# students_polygroup = []
# groups = list(stud.keys())
# for id, group in enumerate(groups):
#     for id2, group2 in enumerate(groups[id+1:], id+1):
#         cross = stud[group] & stud[group2]
#         if cross:
#             cross = ' and '.join(list(stud[group] & stud[group2]))
#             print(f'{group} and {group2} has {cross}')

size = input("Input size you'd like to convert: ")
country = str.title(input("Which country: "))

sizes_dict = {
    "International": ["XXS", "XS", "S", "M", "L", "XL", "XXL", "XXXL"],
    "Russia": ["42", "44", "46", "48", "50", "52", "54", "56"],
    "Germany": ["36", "38", "40", "42", "44", "46", "48", "50"],
    "France": ["38", "40", "42", "44", "46", "48", "50", "52"],
    "Great Britain": ["24", "26", "28", "30", "32", "34", "36", "38"]
}

country_check = country in sizes_dict.keys()
size_check = size in sizes_dict[country]

if country_check:
    if size_check:
        key_size = sizes_dict[country].index(size)
        equivalent_size = sizes_dict["International"][key_size]
        print(f"The International equivalent of {country} size {size} is {equivalent_size}.")
    else:
        print(f"This size is not in the {country} grid.")
else:
    print("This tool supports conversion ONLY to the international sizes for Russia, Germany, France, and Great Britain.")

# for i in sizes_dict[0]