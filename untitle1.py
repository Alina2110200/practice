numbers = input('введите елементы для списка')

numbers_list = numbers.split()

suma_numbers = 0
for number in numbers_list:
    suma_numbers += int(number)

average = suma_numbers / len(numbers_list)

print('сумма: ' , suma_numbers)
print('середне арифметичне: ' , average)