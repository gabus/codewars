# simplify a / b, where a and b can be any int

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


inp = input().split(" ")

num_1 = int(inp[0])
num_2 = int(inp[1])

great_common_divider = gcd(num_1, num_2)

sol_a = num_1 / great_common_divider
sol_b = num_2 / great_common_divider

print("{0} {1}".format(int(sol_a), int(sol_b)))
