from collections import deque


def is_valid(x, y, z):
    if 0 <= z < H and 0 <= y < N and 0 <= x < M:
        if box[z][y][x] == 0:
            return True
    return False


def new_tomato(x, y, z):
    if is_valid(x, y, z):
        queue.append((x, y, z))
        box[z][y][x] = 1
        return 1
    return 0


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append((m, n, h))

count = 0
while queue:
    flag = 0
    for _ in range(len(queue)):
        m, n, h = queue.popleft()
        flag += new_tomato(m + 1, n, h)
        flag += new_tomato(m - 1, n, h)
        flag += new_tomato(m, n + 1, h)
        flag += new_tomato(m, n - 1, h)
        flag += new_tomato(m, n, h + 1)
        flag += new_tomato(m, n, h - 1)
    if flag == 0:
        break
    count += 1

for h in box:
    for n in h:
        if 0 in n:
            count = -1
            break

print(count)
