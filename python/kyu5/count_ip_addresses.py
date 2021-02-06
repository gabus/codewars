# https://www.codewars.com/kata/526989a41034285187000de4

"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one
"""


def ips_between(start: str, end: str) -> int:
    start_x1, start_x2, start_x3, start_x4 = parse_ip_address(start)
    start_range = calculate_ip_range(start_x1, start_x2, start_x3, start_x4)

    end_x1, end_x2, end_x3, end_x4 = parse_ip_address(end)
    end_range = calculate_ip_range(end_x1, end_x2, end_x3, end_x4)

    return end_range - start_range


def parse_ip_address(ip: str) -> tuple[int, int, int, int]:
    x1, x2, x3, x4 = ip.split('.')
    return int(x1), int(x2), int(x3), int(x4)


def calculate_ip_range(x1: int, x2: int, x3: int, x4: int) -> int:
    # Formula!
    return x4 + \
         + x3 * 256 \
         + x2 * 256 * 256 \
         + x1 * 256 * 256 * 256


res1 = ips_between('0.0.0.0', '0.0.1.0')
res2 = ips_between('20.0.0.10', '20.0.1.0')
print(res1)
print(res2)
