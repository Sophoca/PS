import heapq
import sys

input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    item = int(input())
    if item == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, item)

# from queue import PriorityQueue
# import sys
#
# input = sys.stdin.readline
# queue = PriorityQueue()
# for _ in range(int(input())):
#     item = int(input())
#     if item == 0:
#         if queue.empty():
#             print(0)
#         else:
#             print(queue.get())
#     else:
#         queue.put(item)
