import sys
input = sys.stdin.readline

N = int(input())
coord = list(map(int, input().split()))
for idx, val in enumerate(coord):
    coord[idx] = [idx, val]
coord.sort(key=lambda x: x[1])
cur = 0
minVal = coord[0][1]
for el in coord:
    if el[1] != minVal:
        minVal = el[1]
        cur += 1
    el[1] = cur
coord.sort()
for idx, val in coord:
    print(val, end=" ")
