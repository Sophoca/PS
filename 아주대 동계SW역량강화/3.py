N, M = map(int, input().split())
friend = dict()
people = input().split()
people.sort()
for person in people:
  friend[person] = set()
for i in range(M):
  A, B = map(str, input().split())
  friend[A].add(B)
  friend[B].add(A)

result = -1
idxA = 0
idxB = 0
for i in range(N):
  for j in range(i, N):
    if i==j:
      continue
    else:
      if j not in friend[people[i]]:
        length = len(friend[people[i]] & friend[people[j]])
        if length > result:
          result = length
          idxA = i
          idxB = j

print(people[idxA], people[idxB])
print(result)
# print(friend, idxA, idxB)
# print(friend[people[idxA]] & friend[people[idxB]])