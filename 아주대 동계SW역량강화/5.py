T = int(input())

for i in range(T):
  req = list(map(int, input().split('+')))
  req.sort()
  print(*req, sep='+')