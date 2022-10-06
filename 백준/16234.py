# start : 02:32
import sys
sys.setrecursionlimit(10 ** 5)


def get_boundary():
    visited = [[0] * N for _ in range(N)]
    groups = []
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                groups.append([])
                dfs(r, c, groups[-1], visited)

    count = 0
    for group in groups:
        if len(group) > 1:
            count += 1
            move(group)
    return count


def dfs(r, c, group, visited):
    if visited[r][c] == 1:
        return

    visited[r][c] = 1
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    group.append((r, c))
    for idx in range(4):
        next_r = r + dr[idx]
        next_c = c + dc[idx]
        if 0 <= next_r < N and 0 <= next_c < N and L <= abs(nations[r][c] - nations[next_r][next_c]) <= R:
            dfs(next_r, next_c, group, visited)


def move(group):
    total_population = 0
    for r, c in group:
        total_population += nations[r][c]

    new_population = total_population // len(group)
    for r, c in group:
        nations[r][c] = new_population


N, L, R = map(int, input().split())
nations = list(list(map(int, input().split())) for _ in range(N))
answer = 0

while True:
    if get_boundary() == 0:
        break
    answer += 1

print(answer)