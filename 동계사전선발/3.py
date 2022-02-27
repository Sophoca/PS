N = int(input())
visited = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
end = []
answer = []
root = 0

for i in range(N):
    a, b = map(int,input().split())
    if i == 0:
        root = a
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(i):
    visited[i] = 1
    node = graph[i]
    if not node in visited:
        dfs(node)
    elif node in visited:
        end.append(node)
        return True
    return False

dfs(root)

def find(v):
    if v not in answer:
        answer.append(v)
        for w in graph[v]:
          find(w)
    return True

find(end[-1])
print(len(answer))
answer.sort()
for i in answer:
  print(i, end=' ')
