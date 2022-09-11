N = int(input())

total = 1
count = 0

if N != 0:
    while N >= 1:
        total *= N
        while total % 10 == 0:
            total = total // 10
            count += 1
        N -= 1

print(count)
