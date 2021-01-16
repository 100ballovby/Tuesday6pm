def minOfThree(a, b, c):
    if len(a) > len(b) and len(a) > len(c):
        return a
    elif len(b) > len(a) and len(b) > len(c):
        return b
    else:
        return c

print(minOfThree('прао', 'dfdf dfdf w', ' fdfdf'))