import sys


def check(n_table):
    valid = set()
    for row in n_table:
        valid.update(set(row))
        if len(valid) != 1:
            return -1
    return valid.pop()


def count(n_table):
    n = len(n_table)
    status = check(n_table)
    if status == 0:
        C[0] += 1
    elif status == 1:
        C[1] += 1
    else:
        count([n_table[idx][:n//2] for idx in range(n // 2)])
        count([n_table[idx][n//2:n] for idx in range(n // 2)])
        count([n_table[idx][:n//2] for idx in range(n // 2, n)])
        count([n_table[idx][n//2:n] for idx in range(n // 2, n)])


input = sys.stdin.readline
N = int(input())
C = [0, 0]
table = [list(map(int, input().split())) for _ in range(N)]
count(table)
print(C[0])
print(C[1])