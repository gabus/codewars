# Find all dividers for given number n
# 1 <= n <= 10^15

import math

n = int(input())
dividers = []
n_sqrt = int(math.sqrt(n))

for x in range(1, n_sqrt + 1):
    if n % x == 0:
        temp = int(n / x)
        if temp != x:
            dividers.append(x)
            dividers.append(temp)
        else:
            dividers.append(x)

dividers.sort()
print('%s' % ', '.join(map(str, dividers)))
