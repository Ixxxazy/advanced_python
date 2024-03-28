def print_number():
    number = 1
    for i in range(1, 99999999):
        number = number + i
        number = number * i
        number = int(number / i)
    print(number)


print_number()
