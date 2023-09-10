from sys import stdin


def input():
    res = []
    for line in stdin:
        nums = line.strip().split()
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
        sign * square((triangle[0], triangle[1], vertex)) > 0 and \
        sign * square((triangle[1], triangle[2], vertex)) > 0 and \
        sign * square((triangle[2], triangle[0], vertex)) > 0


vertices = input()
print(vertices)
