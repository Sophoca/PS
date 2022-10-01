# start -> 2:05, end -> 3:03
import sys
from collections import defaultdict

input = sys.stdin.readline


def find_adjacent(row, col):
    result = set()
    for i in range(4):
        if 0 <= row + dY[i] < N and 0 <= col + dX[i] < N:
            result.add((row + dY[i], col + dX[i]))
    return result


def find_favorite_cell(student_num):
    candidates = defaultdict(lambda: [])
    for row in range(N):
        for col in range(N):
            if answer[row][col] == 0:
                temp_coord = find_adjacent(row, col)
                count = 0
                for temp_r, temp_c in temp_coord:
                    if answer[temp_r][temp_c] in students[student_num]:
                        count += 1
                candidates[count].append((row, col))
    return sorted(candidates.items(), key=lambda item: item[0], reverse=True)[0]


def find_blank_adjacent_cell(candidate_coords):
    candidates = defaultdict(lambda: [])
    for row, col in candidate_coords:
        temp_coord = find_adjacent(row, col)
        count = 0
        for temp_r, temp_c in temp_coord:
            if answer[temp_r][temp_c] == 0:
                count += 1
        candidates[count].append((row, col))
    return sorted(candidates.items(), key=lambda item: item[0], reverse=True)[0]


def calc_score():
    score = 0
    score_table = [0, 1, 10, 100, 1000]
    for row in range(N):
        for col in range(N):
            candidates = find_adjacent(row, col)
            count = 0
            for temp_r, temp_c in candidates:
                if answer[temp_r][temp_c] in students[answer[row][col]]:
                    count += 1
            score += score_table[count]
    return score


N = int(input())
answer = [[0] * N for _ in range(N)]
dX = [-1, 0, 1, 0]
dY = [0, -1, 0, 1]

students = dict()
for _ in range(N ** 2):
    temp = list(map(int, input().split()))
    students[temp[0]] = set(temp[1:])

for key, values in students.items():
    favorite_friends = find_favorite_cell(key)
    if len(favorite_friends[1]) == 0:
        r, c = favorite_friends[1][0]
        answer[r][c] = key
        print(answer)
        continue
    blank_cells = find_blank_adjacent_cell(favorite_friends[1])
    r, c = blank_cells[1][0]
    answer[r][c] = key

print(calc_score())
