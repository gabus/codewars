import time
import math
from fractions import Fraction

# find number with most dividers (and highest number)

def find_dividers_count(number: int) -> int:
    if number == 0: return 0

    count = 0

    while number % 2 == 0:
        # print("2")
        count += 1
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            count += 1
            number = number / i

    # if number > 2:
        # print(number)
        # print("ERRROR")
        # count += 1

    return count


def run(start: int, end: int) -> int:
    max_number = -1
    max_count = -1

    for num in range(start, end + 1):
        count = find_dividers_count(num)
        if count >= max_count:
            max_number = num
            max_count = count



    return max_number


inp = input().split(" ")
st = time.time()

answer = run(int(inp[0]), int(inp[1]))

print('execution time: {0}s'.format(round(time.time() - st, 2)))
print(answer)


# print(find_dividers_count(10000000))



# def primeFactors(n):
#
#
#
# n = 315234242
# primeFactors(n)

