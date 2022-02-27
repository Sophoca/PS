def calcDist(x1, y1, x2, y2):
  return round(((x2-x1)**2+(y2-y1)**2)**0.5, 2)

X, Y, R = map(int, input().split())
coords = list(list(map(int, input().split())) for i in range(5))

dists = []
for coord in coords:
  dists.append(calcDist(X, Y, coord[0], coord[1]))
minVal = min(dists)
if minVal <= R:
  print(dists.index(minVal) + 1)
else:
  print(-1)