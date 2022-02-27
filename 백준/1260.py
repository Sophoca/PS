from collections import deque


def bfs(root, visited=None):
    if visited is None:
        visited = list()
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    return visited


def dfs(root, visited=None):
    if visited is None:
        visited = list()
    visited.append(root)
    for node in sorted(graph[root]):
        if node not in visited:
            visited = dfs(node, visited)
    return visited


N, M, V = map(int, input().split(" "))
graph = list(list() for row in range(N+1))
for _ in range(M):
    a, b = map(int, input().split(" "))
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

print(graph)
print(*dfs(V))
print(*bfs(V))
