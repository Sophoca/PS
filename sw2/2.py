import sys
input = sys.stdin.readline


def find(group, x):
    if group[x][0] != x:
        return find(group, group[x][0])
    return x


def union(group, a, b):
    p_a = find(group, a)
    p_b = find(group, b)
    if p_a < p_b:
        group[p_b][0] = p_a
    else:
        group[p_a][0] = p_b
    return group


def main():
    N, M, K = map(int, input().split())
    ratings = [0] * (N + 1)
    group = list([i, i] for i in range(N + 1))
    for _ in range(M):
        i, s = map(int, input().split())
        ratings[i] = s
    for _ in range(K):
        a, b = map(int, input().split())
        group = union(group, a, b)
    friend = dict()
    for parent, idx in group:
        if parent not in friend:
            friend[parent] = []
        friend[parent].append(idx)
    for key in friend.keys():
        if key == 0:
            continue
        t_sum = 0
        zero_index = []
        for el in friend[key]:
            if ratings[el] == 0:
                zero_index.append(el)
            else:
                t_sum += ratings[el]
        avg = t_sum // (len(friend[key]) - len(zero_index))
        for el in zero_index:
            ratings[el] = avg
    print(ratings)
    print(sum(ratings[1:]) / (len(ratings) - 1))


if __name__ == "__main__":
    main()