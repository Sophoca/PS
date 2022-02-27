N, M = map(int, input().split(" "))
numbers = []
for i in range(N):
    numbers.append(list(input()))
size = min(N, M) - 1
flag = False
while size > 0:
    for n in range(N - size):
        for m in range(M - size):
            if numbers[n][m] == numbers[n][m + size] == numbers[n + size][m] == numbers[n + size][m + size]:
                flag = True
                break
    if flag:
        break
    size -= 1

print((size + 1) ** 2)
