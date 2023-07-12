number = input('Enter a number: ')
digits = list(number)
exponents = list(range(len(digits) - 1, -1, -1))


result = []
for digit, exponent in zip(digits, exponents):
    result.append(f"{digit} * 10^{exponent}")


formatted_result = ", ".join(result)
print(formatted_result)