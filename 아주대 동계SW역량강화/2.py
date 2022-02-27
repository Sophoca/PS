K = int(input())

results = []
for i in range(K):
  tmp = int(input())
  if tmp == 0:
    results.pop()
  else:
    results.append(tmp)
print(sum(results))