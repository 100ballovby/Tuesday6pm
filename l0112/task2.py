'''Task 2. Найти и посчитать пробелы в собщении'''

message = input('Введите сообщение: ')
summ = 0
summ_of_nums = 0
summ_of_letters = 0
symbols = [' ', ',']

for letter in message:
    if letter in symbols:
        summ += 1
    elif letter.isdigit():
        summ_of_nums += 1
    elif letter in 'aeiou':
        summ_of_letters += 1

print(f'Количество специальных символов в строке: {summ}')
print(f'Количество цифр в строке: {summ_of_nums}')
print(f'Количество гласных букв в строке: {summ_of_letters}')

