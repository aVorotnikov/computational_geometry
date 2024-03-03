from sys import stdin
from queue import Queue


def input():
    res = []
    for line in stdin:
        nums = [int(num) for num in line.strip().split()]
        res.append((nums[0], nums[1], nums[2]))
    return res


def check_correct(triangles):
    if max(max(triangle) for triangle in triangles) == len(triangles) + 1:
        return True
    return False


def is_neighbour(i, j, triangleNum):
    if i == triangleNum + 1 and j == 0:
        return 1
    if j == triangleNum + 1 and i == 0:
        return 1
    if j - i == 1 or i - j == 1:
        return 1
    return 0


def get_coincidence_expectation(triangle, triangleNum):
    return 3 - \
        is_neighbour(triangle[0], triangle[1], triangleNum) - \
        is_neighbour(triangle[1], triangle[2], triangleNum) - \
        is_neighbour(triangle[2], triangle[0], triangleNum)


def build_tree(triangles):
    res = [[] for triangle in triangles]
    pool = []
    for i in range(len(triangles)):
        found = 0
        expectation = get_coincidence_expectation(triangles[i], len(triangles))
        if expectation == found:
            continue
        j = 0
        while j < len(pool):
            candidate = pool[j]
            coincidence = sum(int(num in candidate[0]) for num in triangles[i])
            if 2 == coincidence:
                res[i].append(candidate[1])
                res[candidate[1]].append(i)
                candidate[3] += 1
                if candidate[2] == candidate[3]:
                    del pool[j]
                    j -= 1
                found += 1
                if expectation == found:
                    break
            j += 1
        if expectation != found:
            pool.append([triangles[i], i, expectation, found])
    return res


def dists(vertice, tree):
    res = [-1 for v in tree]
    res[vertice] = 0
    was = Queue()
    was.put(vertice)
    while not was.empty():
        v = was.get()
        dist = res[v]
        for adjacent_vertice in tree[v]:
            if -1 != res[adjacent_vertice]:
                continue
            res[adjacent_vertice] = dist + 1
            was.put(adjacent_vertice)
    return res


def diameter(tree):
    dists0 = dists(0, tree)
    vertice = dists0.index(max(dists0))
    return max(dists(vertice, tree))


def main():
    triangles = input()
    if not check_correct(triangles):
        return
    tree = build_tree(triangles)
    print(diameter(tree))


main()
