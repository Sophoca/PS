import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[0] * (N + 1)]
table += [[0] + list(map(int, input().split())) for _ in range(N)]

for x in range(1, N + 1):
    for y in range(2, N + 1):
        table[x][y] += table[x][y - 1]
for y in range(1, N + 1):
    for x in range(2, N + 1):
        table[x][y] += table[x - 1][y]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(table[x2][y2] - table[x2][y1 - 1] - table[x1 - 1][y2] + table[x1 - 1][y1 - 1])
