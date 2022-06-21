import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]


def union(u, v):
    u = find(u)
    v = find(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v


N, M = map(int, input().split())
parent = list(i for i in range(N + 1))
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
for idx in range(len(parent)):
    parent[idx] = find(parent[idx])
print(len(set(parent[1:])))
