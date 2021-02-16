# 3 simboliu string (a-z) -> md5
# md5 string: 00b03726ba42c3aeaf53df65552eff92

import hashlib

hash = "00b03726ba42c3aeaf53df65552eff92"


# fetch_letter(Null, 3)


def fetch_letter(index: int, string_length: int, word: str):
    abc = 'abcdefghijklmnopqrstuvwxyz'

    if index <= len(abc):
        word
        return fetch_letter(index + 1, 0)



    # for _index in range(len(abc)):
    #     if string_length != 0:
    #         string_length -= 1
    #         return fetch_letter(_index, string_length)
    #     print(abc[_index])

word = fetch_letter(0, 3)
print(word)

# def test_rec(depth: int, word: str) -> str:
#     if depth <= 0:
#         return word
#     word = word + " -> " + str(depth)
#     return test_rec(depth - 1, word)
#
#
# res = test_rec(5, "")
# print(res)

# [0, 27000]:
#     aaa


def generate_hash(str2hash: str) -> str:
    result = hashlib.md5(str2hash.encode())
    return result.hexdigest()
