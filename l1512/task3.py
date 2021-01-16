a = int(input('Введите число: '))
b = int(input('Введите другое число: '))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
print(gcd)