# 이진탐색 문제는 신경을 많이 써야함
# O(N * logC) 이진탐색을 이용해야함 (C의 범위가 10억)

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start = 1
end = house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    value = house[0]
    print(mid)
    for idx in range(N):
        if house[idx] >= value + mid:
            value = house[idx]
            count += 1
    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)























