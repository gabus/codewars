def find_palindromes(start: int, end: int) -> list:
    found = []

    for x in range(start, end + 1):
        if not check_palindromes(str(x)):
            continue

        if not check_palindromes(str(x * x)):
            continue

        found.append(x)

    return found


def check_palindromes(number: str) -> bool:
    return number[::-1] == number


inp = input()
inp_list = inp.split(" ")
palindromes_found = find_palindromes(int(inp_list[0]), int(inp_list[1]))
print(' '.join(map(str, palindromes_found)) if palindromes_found else 0)
