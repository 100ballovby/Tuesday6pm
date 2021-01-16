from time import sleep
n = int(input('Введите число: '))

while n > 0:
    if n % 2 == 0:
        print('Делю на два')
        n = n // 2
        print(n)
        sleep(2)
    else:
        print('Отнимаю 1')
        n = n - 1
        print(n)
        sleep(2)

print('Я закончила!')