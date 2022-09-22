MAX = 1001

N = int(input())
numbers = list(map(int, input().split(' ')))
is_prime = [True for i in range(MAX + 1)]
is_prime[0], is_prime[1] = False, False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX, i):
            is_prime[j] = False

answer = 0
for number in numbers:
    if is_prime[number]:
        answer += 1
print(answer)