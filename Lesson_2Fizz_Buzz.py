fizz = int(input("Enter Fizz: "))
buzz = int(input("Enter Buzz: "))
n = int(input("Enter the last number: "))

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