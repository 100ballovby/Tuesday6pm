x1 = int(input('введите х1: '))
y1 = int(input('введите y1: '))
x2 = int(input('введите х2: '))
y2 = int(input('введите y2: '))

summ = x1 + y1 + x2 + y2

if summ % 2 == 0:
    print('Обе ячейки одного цвета')
else:
    print('Ячейки разных цветов')

