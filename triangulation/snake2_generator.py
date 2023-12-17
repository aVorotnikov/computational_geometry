snake_len = int(input())

for x in range(0, snake_len + 1):
    if x % 4 == 0:
        print(x, 0)
    if x % 4 == 1:
        print(x, 2)
    if x % 4 == 2:
        print(x, 3)
    if x % 4 == 3:
        print(x, 2)

for x in range(snake_len, -1, -1):
    if x % 4 == 0:
        print(x, 1)
    if x % 4 == 1:
        print(x, 3)
    if x % 4 == 2:
        print(x, 4)
    if x % 4 == 3:
        print(x, 3)