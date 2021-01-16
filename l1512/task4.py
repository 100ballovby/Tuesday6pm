'''
Task 4
Найти значение среди списка чисел, которое встречается чаще всего
'''


def from_x_to_DECIMAL(base, number):
    alphabet = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    r1 = 0
    for element in number:
        if element.lower() in alphabet:
            element = alphabet[element]
        result = r1 * base + int(element)
        r1 = result

    return result