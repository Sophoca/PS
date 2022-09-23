SIZE = 50


def solution(commands):
    answer = [[0 for c in range(SIZE)] for r in range(SIZE)]
    parents = [[[r, c] for c in range(SIZE)] for r in range(SIZE)]

    for command in commands:
        segs = command.split(' ')
        type = segs[0]
        params = segs[1:]
        if type == 'UPDATE':
            UPDATE(answer, parents, params)
        elif type == 'MERGE':
            MERGE(answer, parents, params)
        # elif type == 'UNMERGE':
        #     UNMERGE(answer, params)
        # elif type == 'PRINT':
        #     PRINT(answer, params)

    print(answer)
    return answer


def find_parent(answer, parents, r, c, value):
    if parents[r][c][0] != r or parents[r][c][1] != c:
        answer[r][c] = value
        return find_parent(answer, parents, parents[r][c][0], parents[r][c][1], value)
    return [r, c]

# def union_parent(answer, parent, r1, c1, r2, c2, value):
#     pr1, pc1 = find_parent(answer, parent, r1, c1, value)
#     pr2, pc2 = find_parent(answer, parent, r2, c2, value)
#     if pr1 < pr2:
#         parent[pr2][pc2] = [pr1, pc1]
#     else:
#         parent[pr1][pc1] = [pr2, pc2]

def UPDATE(answer, parents, params):
    #값 입력
    if len(params) == 3:
        r = int(params[0]) - 1
        c = int(params[1]) - 1
        answer[r][c] = params[2]
        find_parent(answer, parents, r, c, params[2])
    # 모두 바꾸기
    else:
        for r in range(SIZE):
            for c in range(SIZE):
                if answer[r][c] == params[0]:
                    answer[r][c] = params[1]


def MERGE(answer, parents, params):
    r1, c1, r2, c2 = map(int, params)
    pr1, pc1 = find_parent(answer, parents, r1, c1, )


# def UNMERGE(answer, params):


def PRINT(answer, params):
    result = answer[int(params[0]) - 1][int(params[1]) - 1]
    if result == 0:
        print("EMPTY")
    else:
        print(result)

solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])