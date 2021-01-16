n = 1

while n <= 10:
    n += 1
    # print(f'n = {n}\n')
    if n % 3 == 0:
        print(f'{n} Делится на 3')
    else:
        continue

people = ['Arseniy', 'Den', 'Tim', 'Ben', 'Will', 'John', 'Alfred', 'Андрей']
for name in people:
    if not (name.startswith('A') or name.startswith('B') or name.startswith('А')):
        continue  # пропускает имена, которые не начинаются на А или В
    elif name == 'Will':
        break  # остановится на имени Will
    else:
        print(f'Привет, {name}!')
