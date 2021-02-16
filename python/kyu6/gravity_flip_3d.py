def flip(d: str, a: list):
    if d == 'L' or d == 'R':
        a = flip_l_r(d, a)
    else:
        a = flip_u_d(d, a)

    return a


def flip_l_r(gravity, box):
    for row in box:
        row.sort() if gravity == 'R' else row.sort(reverse=True)

    return row


def flip_u_d(gravity, box):
    new_list = [[] for _ in range(len(box) - 1)]
    index = 0

    for y in range(0, len(box[0])):
        for x in box:
            new_list[index].append(x[y])

        new_list[index].sort() if gravity == 'D' else new_list[index].sort(reverse=True)
        index += 1

    return format_u_d_box(new_list)


def format_u_d_box(box):
    new_list = [[] for _ in range(len(box[0]))]
    index = 0

    for y in range(0, len(box[0])):
        for x in box:
            new_list[index].append(x[y])
        index += 1
    return new_list


"""
-------------- TESTS --------------
"""
def test(a, b):
    if a == b:
        print("SUCCESS")
    else:
        print({
            'Status': "FAILED",
            'Expected': b,
            'Got': a
        })

box = [[1, 3, 2],
       [4, 5, 1],
       [6, 5, 3],
       [7, 2, 9]]

test(flip('R', box), [[1, 2, 3],
                    [1, 4, 5],
                    [3, 5, 6],
                    [2, 7, 9]])

# test(flip('L', box), [[3, 2, 1],
#                     [5, 4, 1],
#                     [6, 5, 3],
#                     [9, 7, 2]])
#
# test(flip('U', box), [[7, 5, 9],
#                     [6, 5, 3],
#                     [4, 3, 2],
#                     [1, 2, 1]])
#
# test(flip('D', box), [[1, 2, 1],
#                     [4, 3, 2],
#                     [6, 5, 3],
#                     [7, 5, 9]])