# check if number has 3 repetitive digits. print them all ascending

# 1000 - 0
# 123114 - 1
# 1545342151 - 1 5

inp = list(input())

found = {}
for numb in inp:
    if numb in found.keys():
        found[numb] = found[numb] + 1
    else:
        found[numb] = 1

correct = [number for number in found if found[number] == 3]
correct.sort()
print(' '.join(correct) if correct else 0)
