# start 02:03 -> end 03:49
from collections import deque, defaultdict


def find_start_coord():
    for r in range(N):
        for c in range(N):
            if space[r][c] == 9:
                space[r][c] = 0
                return (r, c)


def find_possible_coords(cur_coords):
    possible_coords_dist = defaultdict(lambda: [])
    queue = deque([cur_coords])
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    visited = set()
    visited.add(cur_coords)
    dist = 0
    next_queue = set()
    while queue:
        r, c = queue.popleft()

        if space[r][c] < size and space[r][c] != 0:
            possible_coords_dist[dist].append((r, c))
        for dr, dc in d:
            next_r = r + dr
            next_c = c + dc
            if 0 <= next_r < N and 0 <= next_c < N and space[next_r][next_c] <= size and (next_r, next_c) not in visited:
                next_queue.add((next_r, next_c))
                visited.add((next_r, next_c))

        if not queue and next_queue:
            if possible_coords_dist:
                break
            dist += 1
            queue.extend(next_queue)
            next_queue.clear()

    return list(possible_coords_dist.items())


N = int(input())
space = list(list(map(int, input().split())) for _ in range(N))

size = 2
eat_count = 0
time = 0

start_coord = find_start_coord()
while True:
    result = find_possible_coords(start_coord)
    if len(result) == 0:
        break

    # 걸린 시간, 상어가 이동한 위치, 상어 크기 갱신
    spent_time, coords = result[0]
    coords.sort()
    time += spent_time
    start_coord = coords[0]
    space[start_coord[0]][start_coord[1]] = 0
    eat_count += 1
    if eat_count == size:
        size += 1
        eat_count = 0
print(time)
