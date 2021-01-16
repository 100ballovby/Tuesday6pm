for i in range(1500, 2701):
    if i % 7 == 0 and i % 3 == 0:
        print(f'Число {i} делится и на 3: {i / 3}, и на 7: {i / 7}')


'''
*
* *
* * *
* * * *
* * *
* *
*
'''
n = int(input('Впишите число: '))
for i in range(n):
    print('* ' * i)

