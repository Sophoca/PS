from collections import deque


def d(num):
    return 2 * num % 10000


def s(num):
    return 9999 if num == 0 else num - 1


def l(num):
    return num % 1000 * 10 + num // 1000


def r(num):
    return num % 10 * 1000 + num // 10


def bfs():
    queue = deque([A])
    while queue:
        item = queue.popleft()
        if item == B:
            print(dp[item])
            break
        for spell, next_item in [("D", d(item)), ("S", s(item)), ("L", l(item)), ("R", r(item))]:
            if spell == "D" and item == 0:
                continue
            elif dp[next_item] == "":
                dp[next_item] += dp[item] + spell
                queue.append(next_item)


for _ in range(int(input())):
    A, B = map(int, input().split())
    dp = [""] * 10000
    bfs()
