from collections import deque


def is_valid(x, y):
    if 0 <= y < N and 0 <= x < M:
        if box[y][x] == 0:
            return True
    return False


def new_tomato(x, y):
    if is_valid(x, y):
        queue.append((x, y))
        box[y][x] = 1
        return 1
    return 0


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
for n in range(N):
    for m in range(M):
        if box[n][m] == 1:
            queue.append((m, n))

count = 0
while queue:
    flag = 0
    for _ in range(len(queue)):
        m, n = queue.popleft()
        flag += new_tomato(m + 1, n)
        flag += new_tomato(m - 1, n)
        flag += new_tomato(m, n + 1)
        flag += new_tomato(m, n - 1)
    if flag == 0:
        break
    count += 1

for n in box:
    if 0 in n:
        count = -1
        break

print(count)
