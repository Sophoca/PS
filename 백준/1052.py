N, K = map(int, input().split())

for _ in range(K - 1):
    count = 1
    while count <= N // 2:
        count *= 2
    if N - count == 0:
        break
    N -= count

count = 1
while count < N:
    count *= 2
    if N - count == 0:
        break

print(count - N)