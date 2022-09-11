import sys
input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    for k in range(K):
        menu = [0] * (M - k)
        for ratings in table:
            for idx, rating in enumerate(ratings):
                if rating >= 5:
                    menu[idx] += 1
        max_index = menu.index(min(menu))
        l_index_list = []
        for idx, ratings in enumerate(table):
            ratings.pop(max_index)
            flag = False
            for rating in ratings:
                if rating >= 5:
                    flag = True
                    break
            if not flag:
                l_index_list.append(idx)
        for l_index in l_index_list:
            table.pop(l_index)
    print(len(table))


if __name__ == "__main__":
    main()