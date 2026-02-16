numbers = input('введите числа')
numbers_list = numbers.split()

suma = 0
for i in numbers_list:
    number = int(i)
if number > 0:
    suma += number

print("Сумма додатних чисел:", suma)