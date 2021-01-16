"""Task 3. Факториал числа"""

# 3! = 1 * 2 * 3
n = int(input('Вводите число: '))

res = 1
for i in range(1, n + 1):
    res *= i
print(f'{n}! = {res}')