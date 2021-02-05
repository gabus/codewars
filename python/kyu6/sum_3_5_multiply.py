# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number: int) -> int:
    _sum = []

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            _sum.append(i)

    return sum(_sum)


print({"10": solution(-10)})  # 23
print({"15": solution(15)})  # [3, 5, 6, 9, 10, 12] = 60
print({"20": solution(20)})  #
print({"20": solution(3498572)})  #
