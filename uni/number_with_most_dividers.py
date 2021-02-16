# find number with most dividers (and highest number)

def find_dividers_count(number: int) -> int:
    if number == 0: return 0

    count = 0

    while number > 1:

        if number % 2 == 0:
            number /= 2
            count += 1
            continue

        if number % 3 == 0:
            number /= 3
            count += 1
            continue

        if number % 5 == 0:
            number /= 5
            count += 1
            continue

        if number % 7 == 0:
            number /= 7
            count += 1
            continue

        return 1

    return count


def run(start: int, end: int):
    max_number = -1
    max_count = -1

    for num in range(start, end + 1):
        count = find_dividers_count(num)
        if count >= max_count:
            max_number = num
            max_count = count

    return max_number


inp = input().split(" ")
answer = run(int(inp[0]), int(inp[1]))
print(answer)
