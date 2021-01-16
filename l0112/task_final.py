numbers = input('Введите числа с пробелами: ')

lst = numbers.split()

for n in lst:
    if int(n) % 2 == 0:
        pass
    else:
        print(f'Число {lst.index(n) + 1} отличчается')

print(lst)