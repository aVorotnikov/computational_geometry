from sys import stdin


def input():
    res = []
    for line in stdin:
        nums = line.strip().split()
        res.append((nums[0], nums[1]))
    return res


print(input())
