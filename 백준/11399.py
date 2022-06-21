N = int(input())
people = list(map(int, input().split()))
people.sort()
# print(people)
for idx in range(1, N):
    people[idx] += people[idx - 1]
print(sum(people))
