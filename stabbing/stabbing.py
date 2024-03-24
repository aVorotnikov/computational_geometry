from sys import stdin
from queue import Queue


def input():
    res = []
    for line in stdin:
        res.append([int(num) for num in line.strip().split()][1:])
    return res


def rotate(diameters):
    new_start = 0
    for i in range(len(diameters)):
        if 0 == len(diameters[i]):
            new_start = i
            break

    if new_start == 0:
        return diameters

    res = []
    for i in range(len(diameters)):
        node = []
        point = (new_start + i) % len(diameters)
        for j in range(len(diameters[point])):
            node.append((len(diameters) + diameters[point][j] - new_start) % len(diameters))
        res.append(node)
    return res


def build_tree(diameters):
    if 2 >= len(diameters):
        raise RuntimeError("No polygon")
    if 3 == len(diameters):
        return [[]]

    diameters = rotate(diameters)
    res = [[] for i in range(len(diameters) - 2)]
    elder_element = 0
    status = [0]
    for i in range(len(diameters)):
        in_diameters = sum(diameter < i for diameter in diameters[i])
        for j in range(in_diameters):
            status.pop()
        out_diameters = len(diameters[i]) - in_diameters
        for j in range(out_diameters):
            elder_element += 1
            last = status[-1]
            status.append(elder_element)
            res[last].append(elder_element)
            res[elder_element].append(last)
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
    diameters = input()
    tree = build_tree(diameters)
    print(diameter(tree))


main()
