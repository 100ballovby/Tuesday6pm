'''
if выражение:
--->тело_условия
else:
--->тело_условия_2
'''

a = int(input('Введите число: '))
b = int(input('Введите число: '))

if a % 2 == 0 and b % 2 == 0:
    print('Оба числа четные!')
else:
    print('Одно число не является четным!')

'''
Task 1.
Напишите программу, которая сравнивает два числа и пишет, 
какое из них меньше.
'''
c = int(input('Введите число: '))

if a < b and a < c:
    print(a)
if b < a and b < c:
    print(c)