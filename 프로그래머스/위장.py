def solution(clothes):
    answer = 1
    comb = dict()
    for cloth in clothes:
        if cloth[1] not in comb:
            comb[cloth[1]] = []
        comb[cloth[1]].append(cloth[0])
    for num in comb.values():
        answer *= len(num)

    return answer - 1
