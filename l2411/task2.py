"""Task 2. Вывести все числа от 0 до 6, кроме 3 и 6"""

for number in range(7):
    if number == 3 or number == 6:
        continue
    print(number)