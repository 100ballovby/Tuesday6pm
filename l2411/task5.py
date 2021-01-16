'''Task 5. Количество нулей'''

zeros = 0
for i in range(int(input('Сколько чисел вводить будем? '))):
    if int(input(f'Введите число {i + 1}: ')) == 0:
        zeros += 1

print(f'Вы ввели {zeros} нулей.')