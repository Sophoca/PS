t=int(input())
array=list()
for _ in range(t):
    a, b=map(int, input().split())
    array.append((a, b))
array.sort()
for i in array:
    print(i[0], i[1])