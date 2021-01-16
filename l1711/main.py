def taxRate(p, t):
    res = round(p * (t / 100), 2)
    return f'Сумма налога {res}$,\nВсего нужно оплатить {res + p}$'


n = int(input('Сколько покупок вы совершили? '))
tax = int(input('Введите ставку в процентах: '))

for item in range(n):
    price = float(input('Введите цену товара: '))

    print(f'Товар №{item + 1}\n\n')
    print(taxRate(p=price, t=tax))




