# start: 18:29 -> end: 20:30

# UP: 1, DOWN: 2, LEFT: 3, RIGHT: 4
def combine(direction, input_blocks):
    r_start, r_end, r_step = 0, 0, 0
    c_start, c_end, c_step = 0, 0, 0
    max_value = 0
    new_blocks = [[0] * N for _ in range(N)]

    if direction == 1 or direction == 2:
        if direction == 1:
            r_start, r_end, r_step = 0, N, 1
        elif direction == 2:
            r_start, r_end, r_step = N - 1, -1, -1
        c_start, c_end, c_step = 0, N, 1

        for c in range(c_start, c_end, c_step):
            stack = []
            for r in range(r_start, r_end, r_step):
                if input_blocks[r][c] != 0:
                    stack.append(input_blocks[r][c])
            temp = []
            for idx in range(len(stack)):
                if idx != len(stack) - 1 and stack[idx] == stack[idx + 1]:
                    temp.append(stack[idx] * 2)
                    stack[idx + 1] = 0
                    continue
                if stack[idx] != 0:
                    temp.append(stack[idx])
            for idx, r in enumerate(range(r_start, r_end, r_step)):
                if idx < len(temp):
                    new_blocks[r][c] = temp[idx]
                    max_value = max(max_value, temp[idx])

    else:
        r_start, r_end, r_step = 0, N, 1
        if direction == 3:
            c_start, c_end, c_step = 0, N, 1
        elif direction == 4:
            c_start, c_end, c_step = N - 1, -1, -1

        for r in range(r_start, r_end, r_step):
            stack = []
            for c in range(c_start, c_end, c_step):
                if input_blocks[r][c] != 0:
                    stack.append(input_blocks[r][c])
            temp = []
            for idx in range(len(stack)):
                if idx != len(stack) - 1 and stack[idx] == stack[idx + 1]:
                    temp.append(stack[idx] * 2)
                    stack[idx + 1] = 0
                    continue
                if stack[idx] != 0:
                    temp.append(stack[idx])
            for idx, c in enumerate(range(c_start, c_end, c_step)):
                if idx < len(temp):
                    new_blocks[r][c] = temp[idx]
                    max_value = max(max_value, temp[idx])

    return max_value, new_blocks


def dfs(direction, step, cur_blocks):
    if step > 5:
        return
    result, new_blocks = combine(direction, cur_blocks)

    if result > answer[0]:
        answer[0] = result

    for idx in range(1, 5):
        dfs(idx, step + 1, new_blocks)


N = int(input())
blocks = list(list(map(int, input().split())) for _ in range(N))
answer = [0]

for i in range(1, 5):
    dfs(i, 1, blocks)

print(answer[0])
