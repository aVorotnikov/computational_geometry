snake_len = int(input())

for x in range(0, snake_len + 1):
    print(x, 0 if x % 2 == 0 else 2)

for x in range(snake_len, -1, -1):
    print(x, 1 if x % 2 == 0 else 3)