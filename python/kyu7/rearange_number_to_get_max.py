def max_redigit(num: int):
    if 100 > num or num > 999:
        return None

    t = list(str(num))
    t.sort(reverse=True)
    return int(''.join(t))


if max_redigit(123) == 321:
    print("SUCCESS")
else:
    print("FAILED")

if max_redigit(555) == 555:
    print("SUCCESS")
else:
    print("FAILED")