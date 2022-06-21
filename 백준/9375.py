def solution(clothes):
    comb = dict()
    for cloth in clothes:
        if cloth[1] not in comb:
            comb[cloth[1]] = []
        comb[cloth[1]].append(cloth[0])
    answer = 1
    for num in comb.values():
        answer *= len(num) + 1

    return answer - 1


for _ in range(int(input())):
    N = int(input())
    clothes = list(input().split() for _ in range(N))
    print(solution(clothes))
