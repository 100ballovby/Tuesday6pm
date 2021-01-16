def multi_arg(*numbers):
    sum = 0

    for number in numbers:
        sum += number
    return f'Сумма чисел: {sum}'


print(multi_arg(10, 12, 13, 15, 16, 17))
'''
* - args - передать аргументы кортежем;
** - kwargs - передать аргументы словарем;
'''


def db_response(**data):
    for key, value in data.items():
        print(f'{key} is {value}')
    return None


db_response(fn='John', sn='Dory', age=50, ph='+375291234567')


def remove_blanks(text):
    return text.replace(' ', '')  # заменяет пробелы на пустоту


def remove_spaces(text):
    new_text = ''
    for symbol in text:
        if symbol != ' ': new_text += symbol
    return new_text


print(remove_blanks('+375 (29) 531 22 56'))
print(remove_spaces('+375 (29) 531 22 56'))
