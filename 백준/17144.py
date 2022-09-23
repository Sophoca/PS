# start -> 18:56
# end -> 20:43

def spread():
    next_room = [[0] * C for _ in range(R)]
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for r in range(R):
        for c in range(C):
            if room[r][c] < 5:
                continue
            count = 0
            sub_dust = room[r][c] // 5
            for dr, dc in d:
                if 0 <= r + dr < R and 0 <= c + dc < C and room[r + dr][c + dc] != -1:
                    next_room[r + dr][c + dc] += sub_dust
                    count += 1
            room[r][c] -= sub_dust * count
    for r in range(R):
        for c in range(C):
            room[r][c] += next_room[r][c]

def rotate():
    room[air_cleaner_col][0], room[air_cleaner_col + 1][0] = 0, 0
    # temp1
    for r in range(air_cleaner_col - 1, 0, -1):
        room[r][0] = room[r - 1][0]
    for c in range(0, C - 1):
        room[0][c] = room[0][c + 1]
    for r in range(0, air_cleaner_col):
        room[r][C - 1] = room[r + 1][C - 1]
    for c in range(C - 1, 0, -1):
        room[air_cleaner_col][c] = room[air_cleaner_col][c - 1]

    # temp2
    for r in range(air_cleaner_col + 2, R - 1):
        room[r][0] = room[r + 1][0]
    for c in range(0, C - 1):
        room[R - 1][c] = room[R - 1][c + 1]
    for r in range(R - 1, air_cleaner_col + 1, -1):
        room[r][C - 1] = room[r - 1][C - 1]
    for c in range(C - 1, 0, -1):
        room[air_cleaner_col + 1][c] = room[air_cleaner_col + 1][c - 1]

def count_dust():
    result = 0
    for row in room:
        result += sum(row)
    return result

def print_room():
    for row in room:
        print(row)
    print('-----------')

R, C, T = map(int, input().split())
room = list(list(map(int, input().split())) for _ in range(R))
air_cleaner_col = 0
for idx, row in enumerate(room):
    if row[0] == -1:
        air_cleaner_col = idx
        break
for _ in range(T):
    spread()
    # print_room()
    rotate()
    # print_room()
    # print('------')
print(count_dust())
