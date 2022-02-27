N = int(input())
weights = list(map(int, input().split(" ")))
weights.sort()

temp = 0
for obj in weights:
    if obj > temp + 1:
        break
    else:
        temp += obj
print(temp + 1)
