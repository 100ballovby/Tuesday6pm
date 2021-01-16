'''
Введите число: --> 6

6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
'''
n = int(input('Введите число: '))

for number in range(1, 11):
    print(f'{n} x {number} = {n * number}')