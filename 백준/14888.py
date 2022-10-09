# start 01:49 -> end 02:02

import math
import copy

MAX = math.inf
MIN = -math.inf


def dfs(idx, total, remain_ops):
    if idx == N:
        answers.append(total)
    # print(idx, total, remain_ops)
    for op_idx, op_count in enumerate(remain_ops):
        new_ops = copy.deepcopy(remain_ops)
        if op_count == 0:
            continue
        new_ops[op_idx] -= 1
        new_total = total
        if op_idx == 0:
            new_total += A[idx]
        elif op_idx == 1:
            new_total -= A[idx]
        elif op_idx == 2:
            new_total *= A[idx]
        else:
            if new_total < 0 and A[idx] > 0:
                new_total = (-1 * new_total // A[idx]) * -1
            else:
                new_total //= A[idx]
        dfs(idx + 1, new_total, new_ops)


N = int(input())
A = list(map(int, input().split()))
op_counts = list(map(int, input().split()))
answers = []

dfs(1, A[0], op_counts)
print(max(answers))
print(min(answers))