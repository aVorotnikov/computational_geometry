from sys import stdin


def input():
    res = []
    for line in stdin:
        nums = [int(num) for num in line.strip().split()]
        res.append((nums[0], nums[1]))
    return res


def square(triangle):
    return \
        triangle[0][0] * triangle[1][1] + \
        triangle[0][1] * triangle[2][0] + \
        triangle[1][0] * triangle[2][1] - \
        triangle[1][1] * triangle[2][0] - \
        triangle[0][0] * triangle[2][1] - \
        triangle[1][0] * triangle[0][1]


def check_vertex_in_triangle(vertex, triangle):
    sign = 1 if square(triangle) > 0 else -1
    return \
        sign * square((triangle[0], triangle[1], vertex)) >= 0 and \
        sign * square((triangle[1], triangle[2], vertex)) >= 0 and \
        sign * square((triangle[2], triangle[0], vertex)) >= 0


def check_ear(vertices, ignore_start):
    triangle = [vertices[i % len(vertices)] for i in range(ignore_start, ignore_start + 3)]
    if square(triangle) < 0:
        return False
    ignore_end = (ignore_start + 2) % len(vertices) + 1
    if ignore_start < ignore_end:
        for i in range(0, ignore_start):
            if check_vertex_in_triangle(vertices[i], triangle):
                return False
        for i in range(ignore_end, len(vertices)):
            if check_vertex_in_triangle(vertices[i], triangle):
                return False
    else:
        for i in range(ignore_end, ignore_start):
            if check_vertex_in_triangle(vertices[i], triangle):
                return False
    return True


def print_triangle(triangle):
    for i in range(0, len(triangle)):
        print(triangle[i][0], triangle[i][1], end=" ")
    print("")


def print_triangle_index(vertices, ignore_start):
    print_triangle([vertices[i % len(vertices)] for i in range(ignore_start, ignore_start + 3)])


def triangulation(vertices):
    if len(vertices) < 3:
        return
    while (3 < len(vertices)):
        for i in range(0, len(vertices)):
            if check_ear(vertices, i):
                print_triangle_index(vertices, i)
                del vertices[(i + 1) % len(vertices)]
                break
    print_triangle(vertices)


triangulation(input())
