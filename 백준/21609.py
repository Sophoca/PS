# start -> 16:20
import math


def dfs(r, c, color, group):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    if visited[r][c] == 1 or (blocks[r][c] != 0 and blocks[r][c] != color):
        return

    if blocks[r][c] == 0:
        if (r, c) in group['rainbow_coords']:
            return
        group['rainbow_coords'].append((r, c))
    else:
        visited[r][c] = 1
        group['colored_coords'].append((r, c))

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < len(blocks) and 0 <= nc < len(blocks[0]):
            dfs(nr, nc, color, group)


def find_largest_block():
    groups = []
    for r in range(len(blocks)):
        for c in range(len(blocks[0])):
            if visited[r][c] == 0 and blocks[r][c] != -1 and blocks[r][c] != 0 and blocks[r][c] != -math.inf:
                groups.append({'colored_coords': [], 'rainbow_coords': []})
                color = blocks[r][c]
                dfs(r, c, color, groups[-1])

    # print(groups)

    results = []
    for group in groups:
        clen = len(group['colored_coords'])
        rlen = len(group['rainbow_coords'])
        if clen + rlen < 2:
            continue
        results.append((clen + rlen, rlen, sorted(group['colored_coords']), group['rainbow_coords']))
    if len(results) == 0:
        return -1

    results.sort(key=lambda x: (x[0], x[1], x[2][0]))
    return results[-1]


def remove_block(coords):
    for r, c in coords:
        blocks[r][c] = -math.inf


def gravity():
    R = len(blocks)
    C = len(blocks[0])
    for c in range(C):
        for r in range(R - 1, 0, -1):
            if blocks[r][c] != -math.inf:
                continue
            t = r - 1
            while t >= 0:
                if blocks[t][c] == -1:
                    break
                if blocks[t][c] == -math.inf:
                    t -= 1
                    continue
                blocks[r][c] = blocks[t][c]
                blocks[t][c] = -math.inf
                break


def rotate():
    C = len(blocks)
    R = len(blocks[0])
    new_blocks = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            new_blocks[r][c] = blocks[c][R - r - 1]

    return new_blocks


N, M = map(int, input().split())
blocks = list(list(map(int, input().split())) for _ in range(N))
score = 0

while True:
    visited = [[0] * len(blocks[0]) for _ in range(len(blocks))]
    result = find_largest_block()

    # print(result)

    if result == -1:
        break

    result[2].extend(result[3])
    remove_block(result[2])
    score += result[0] ** 2
    gravity()
    blocks = rotate()
    gravity()

    # print(blocks)

print(score)




