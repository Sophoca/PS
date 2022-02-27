# c의 범위가 10억이기에 O(M * log(c))를 만족해야 시간제한 안걸림
# BFS 활용 O(M)

N, M=map(int, input().split(' '))

def bfs(weight):
    queue=[start_node]
    visited=[0]*(N+1)
    visited[start_node]=1
    while queue:
        a=queue.pop(0)
        for b, c in bridge[a]:
            if visited[b]==0 and c>=weight:
                visited[b]=1
                queue.append(b)
    return visited[end_node]

bridge=[[] for _ in range(N+1)]
minWeight=100000; maxWeight=1

for _ in range(M): # a, b, c(중량)
    a, b, c=map(int, input().split(' '))
    bridge[a].append((b, c))
    bridge[b].append((a, c))
    minWeight=min(minWeight, c)
    maxWeight=max(maxWeight, c)

start_node, end_node=map(int, input().split())
result=minWeight
while minWeight<=maxWeight:
    mid=(minWeight+maxWeight)//2
    if bfs(mid):    # 경로가 존재하는 경우, 중량을 증가시킴
        minWeight=mid+1
        result=mid
    else:   # 경로가 존재하지 않는 경우, 중량을 감소시킴
        maxWeight=mid-1
print(result)