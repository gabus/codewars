# given n > 7, following must be true: 3a + 5b = n

def run(n):
    # n = int(input)

    fives_counter = 0
    while n % 3 != 0:
        n -= 5
        fives_counter += 1

    _a = n / 3
    _b = fives_counter

    return int(_a), _b

test = 21
a, b = run(test)
print({'a': a, 'b': b})
print({"3a + 5b = n": str(3 * a + 5 * b), 'must be equal: ': test})
