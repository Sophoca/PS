import sys

input = sys.stdin.readline

N = int(input())
tree = [0] * 100001
for _ in range(N + 1):
    a, b = map(int, input().split())
    tree[b] = a
