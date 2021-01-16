'''Task 1. Найти все числа, которые делятся на 3 или на 5 в заданном диапазоне'''

ran = int(input('Впишите число: '))

for number in range(1, ran):
    if number % 3 == 0 or number % 5 == 0:
        print(number)

