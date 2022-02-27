N = int(input())
arr = []
isPlus = True
isX = True
mid = int(N/2)

for _ in range(N):
  arr.append(list(map(int, input().split())))

for i in range(N):
  for j in range(N):
    if i==j:
      if not (arr[i][j]==1 and arr[i][N-i-1]==1):
        isX = False
        print('check X', i, j)
    if i==mid or j==mid:
      if arr[i][j]!=1:
        isPlus = False
        print('check +', i, j)

if not isPlus ^ isX:
  print(2)
elif isPlus:
  print(0)
else:
  print(1)