numbers = input("Введите числа через пробел: ")
numbers_list = numbers.split()

unique_list = []

for num in numbers_list:
    number = int(num)
    
    if number not in unique_list:
        unique_list.append(number)

print("Уникальные элементы:", unique_list)
