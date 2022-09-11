def insert(struct, k, S):
    struct[0]['data'][k] = S
    avalanche(struct)


def find(struct, k):
    for idx, obj in enumerate(struct):
        if k in obj['data']:
            print(idx + 1, obj['data'][k])
            return
    print('None')


def avalanche(struct, idx=0):
    if idx == len(struct) - 1:
        return
    elif struct[idx]['size'] < sum(struct[idx]['data'].values()):
        cur_level = struct[idx]
        temp = cur_level['data']
        cur_level['data'] = dict()
        for key in temp.keys():
            struct[idx + 1]['data'][key] = temp[key]
        avalanche(struct, idx + 1)

    return


def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))
    C.append(0)
    struct = [{"size": C[idx], "data": {}} for idx in range(len(C))]

    for _ in range(Q):
        query = input().split()
        if len(query) == 3:
            insert(struct, int(query[1]), int(query[2]))
        else:
            find(struct, int(query[1]))


if __name__ == "__main__":
    main()