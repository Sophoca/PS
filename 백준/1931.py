import sys

input = sys.stdin.readline
table = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    table.append([a, b])
table.sort(key=lambda x: (x[1], x[0]))
count = 1
end_time = table[0][1]
for idx in range(1, len(table)):
    if table[idx][0] >= end_time:
        end_time = table[idx][1]
        count += 1
print(count)