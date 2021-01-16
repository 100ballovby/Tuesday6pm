def digital_root(number):
    while number >= 10:
        number = sum(int(i) for i in str(number))
    return number


def digital_root_2(number):
    return number % 9

print(digital_root(942))