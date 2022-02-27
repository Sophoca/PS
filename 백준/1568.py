N = int(input())
result = 0
num = 1
while N > 0:
    if N < num:
        num = 1
    N -= num
    num += 1
    result += 1
print(result)