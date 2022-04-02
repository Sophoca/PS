MAX = 100000
N = int(input())
tree = list(list(map(int, input().split())) for _ in range(N))
print(tree)
dp = list([0] * (N + 1) for _ in range(N + 1))
for idx in range(N):
