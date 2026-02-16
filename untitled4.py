numbers = input('введите числа: ')
numbers_list = numbers.split()

for i in range(len(numbers_list)):
    if int(numbers_list[i]) % 2:
        print('индекс: ' , i)