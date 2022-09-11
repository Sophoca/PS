from collections import deque
MAX = 10 ** 5


def bfs():
    queue = deque([N])
    while queue:
        item = queue.popleft()
        if item == K:
            print(count[item])
            break
        for next_item in (item + 1, item - 1, item * 2):
            if 0 <= next_item <= MAX and not count[next_item]:
                count[next_item] = count[item] + 1
                queue.append(next_item)


N, K = map(int, input().split())
count = [0] * (MAX + 1)
bfs()
