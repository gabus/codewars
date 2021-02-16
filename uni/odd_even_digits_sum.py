# given n, check if sum of n digits ir odd or even

# 1 - YES
# 2 - NO

inp = list(input())
inp_sum = sum(map(int, inp))
print('YES' if inp_sum % 2 == 0 else 'No')
