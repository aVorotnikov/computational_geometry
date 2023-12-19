from sys import stdin


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


def build_tree(triangles):
    res = [[] for triangle in triangles]
    for i in range(len(triangles)):
        for j in range(i):
            coincidence = sum(int(num in triangles[j]) for num in triangles[i])
            if 2 == coincidence:
                res[i].append(j)
                res[j].append(i)
    return res


def dists(vertice, tree):
    res = [-1 for v in tree]
    res[vertice] = 0
    was = [vertice]
    while len(was) > 0:
        v = was[0]
        dist = res[v]
        was = was[1:]
        for adjacent_vertice in tree[v]:
            if -1 != res[adjacent_vertice]:
                continue
            res[adjacent_vertice] = dist + 1
            was.append(adjacent_vertice)
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
