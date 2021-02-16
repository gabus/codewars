# https://www.codewars.com/kata/5579e6a5256bac65e4000060

"""
5
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1
"""


# (2n-1)
def pattern(n):
    if n <= 0:
        return ''

    patern = {}

    for it in range(n):
        patern[it] = []
        nth_pos = n - it - 1
        for t in range(nth_pos):
            patern[it].append(" ")

        # todo cia blogai:
        patern[it].append(fetch_row(it + 1))

    return patern


def fetch_row(nth) -> list:
    half = []
    index = 1
    for _ in range(nth):
        half.append(index)
        index += 1
        if index >= 10:
            index = 0

    other_half = half[0:-1]
    other_half.reverse()

    return half + other_half


x = pattern(5)
print(x)

