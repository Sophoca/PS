chess = [1, 1, 2, 2, 2, 8]
temp_chess = list(map(int, input().split()))
for idx in range(len(chess)):
    print(chess[idx] - temp_chess[idx], end=' ')