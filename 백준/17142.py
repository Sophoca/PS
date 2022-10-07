# start: 21:12
from itertools import combinations
from collections import deque
import copy
import math

N, M = map(int, input().split())
lab = list(list(map(int, input().split())) for _ in range(N))

virus_candidate = set()
answer = math.inf

# virus 후보 좌표 추출
for row in range(N):
    for col in range(N):
        if lab[row][col] == 2:
            virus_candidate.add((row, col))
virus_candidate = set(combinations(virus_candidate, M))

dR = [1, 0, -1, 0]
dC = [0, 1, 0, -1]

# virus 후보 완전 탐색
for virus in virus_candidate:
    temp_lab = copy.deepcopy(lab)

    queue = deque([])
    for init in virus:
        queue.append(init)
        temp_lab[init[0]][init[1]] = 1

    next_coords = set()
    next_viruses = set()
    count = 0

    # virus 전파, 시간 계산
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            next_r = r + dR[idx]
            next_c = c + dC[idx]
            if 0 <= next_r < N and 0 <= next_c < N and temp_lab[next_r][next_c] != 1:
                if temp_lab[next_r][next_c] == 0:
                    next_coords.add((next_r, next_c))
                else:
                    next_viruses.add((next_r, next_c))
                temp_lab[next_r][next_c] = 1

        # 다음 초에 전파될 바이러스 좌표를 큐에 추가
        if not queue:
            if next_coords:
                count += 1
                for next_coord in next_coords:
                    queue.append(next_coord)
                for next_virus in next_viruses:
                    queue.append(next_virus)
                next_coords = set()
                next_viruses = set()
            elif next_viruses:
                is_zero_exist = False
                for row in temp_lab:
                    for value in row:
                        if value == 0:
                            is_zero_exist = True
                            break
                if is_zero_exist:
                    count += 1
                    for next_virus in next_viruses:
                        queue.append(next_virus)
                    next_viruses = set()

    # 도달할 수 없는 방 확인, 최단시간 업데이트
    is_zero_exist = False
    for row in temp_lab:
        for value in row:
            if value == 0:
                is_zero_exist = True
                break

    if not is_zero_exist:
        answer = min(answer, count)

if answer == math.inf:
    answer = -1
print(answer)


