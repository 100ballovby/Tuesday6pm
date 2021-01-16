a = int(input('Введите число 1'))
b = int(input('Введите число 2'))
c = int(input('Введите число 3'))

if a == b == c:
    print('Все числа равны')
elif a == b or b == c or a == c:
    print('Два числа равны')
else:
    print('Числа не равны')