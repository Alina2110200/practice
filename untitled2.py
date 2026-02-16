numbers = input("Введите числа: ")
numbers_list = numbers.split()

target = int(input("введите число, которое нужно найти: "))

count = 0
for number in numbers_list:
    if int(number) == target:
        count += 1

print('количество:' , count)