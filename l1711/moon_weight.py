'''
Если бы вы сейчас были на луне, ваш вес составил бы 16.5% от земного.
Чтобы узнать, сколько это, умножьте свой земной вес на 0.165.
Если бы каждый год в течение следующих 15 лет вы прибавляли по одному килограмму веса,
каким бы оказался ваш лунный вес в каждый из ежегодных визитов на Луну вплоть до 15 года?
'''

weight = int(input('Введите свой вес: '))

for year in range(15):
    weight += 1
    moonlight_weight = weight * 0.165
    print(f'Визит №{year}, вес на луне {moonlight_weight}')