def solution(movie):
    count = dict()
    for obj in movie:
        if obj not in count:
            count[obj] = 0
        count[obj] += 1

    answer = list(map(lambda x: x[0], sorted(count.items(), key=lambda item: (-item[1], item[0]))))
    print(answer)

    return answer

solution(["spy","ray","spy","room","once","ray","spy","once"])
