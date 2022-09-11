def dfs(x, y):
    if x == -1 or y == -1 or x == M or y == N:
        return
    elif table[y][x] == 1:
        table[y][x] += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    table = [[0] * M for i in range(N)]
    count = 0
    check = [list(map(int, input().split())) for _ in range(K)]
    for m, n in check:
        table[n][m] = 1
    for m, n in check:
        if table[n][m] == 1:
            count += 1
            dfs(m, n)
    print(count)