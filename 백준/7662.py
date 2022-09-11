import sys
import heapq

input = sys.stdin.readline
for _ in range(int(input())):
    maxH, minH = [], []
    N = int(input())
    visited = [False] * N
    for idx in range(N):
        op, val = input().split()
        if op == 'I':
            heapq.heappush(maxH, (-int(val), idx))
            heapq.heappush(minH, (int(val), idx))
            visited[idx] = True
        elif op == 'D':
            if int(val) == 1:
                while maxH and not visited[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    visited[maxH[0][1]] = False
                    heapq.heappop(maxH)
            else:
                while minH and not visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]] = False
                    heapq.heappop(minH)
        print(idx, maxH, minH)

    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    if len(maxH) == 0 or len(minH) == 0:
        print('EMPTY')
    else:
        print(-heapq.heappop(maxH)[0], heapq.heappop(minH)[0])
