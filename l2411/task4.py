"""Task 4. Сумма факториалов"""

n = int(input('Введите число: '))
partial_factorial = 1
partial_sum = 0

for factorial in range(1, n + 1):
    partial_factorial *= factorial
    print(f'{factorial}! = {partial_factorial}')
    partial_sum += partial_factorial
    print(f'Сумма факториалов = {partial_sum}\n')