import sys

input = sys.stdin.readline


def get_adjacent_index(r, c):
    indexes = []
    if r - 1 >= 0:
        if c - 1 >= 0:
            indexes.append(answers[r - 1][c - 1])
        elif c + 1 < N:
            indexes.append(answers[r - 1][c + 1])
    elif r + 1 < N:
        if c - 1 >= 0:
            indexes.append(answers[r + 1][c - 1])
        elif c + 1 < N:
            indexes.append(answers[r + 1][c + 1])


N = int(input())
params = list(list(map(int, input().split(' '))) for _ in range(N ** 2))
students = dict()
answers = list([0] * N for _ in range(N))

for param in params:
    students[param[0]] = param[1:]


print(students, answers)

# for key, value in students.items()