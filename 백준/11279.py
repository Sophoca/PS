import sys
import heapq

input = sys.stdin.readline
tree = []
for _ in range(int(input())):
    item = int(input())
    if item == 0:
        if len(tree) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(tree))
    else:
        heapq.heappush(tree, -item)
