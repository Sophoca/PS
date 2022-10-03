N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for applier_num in A:
    applier_num -= B
    answer += 1
    if applier_num > 0:
        answer += applier_num // C
        if applier_num % C != 0:
            answer += 1

print(answer)