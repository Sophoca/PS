t=int(input())
array=list()
for i in range(t):
    array.append(list(input().split()))
    array[i][0]=int(array[i][0])
array.sort(key=lambda x: x[0])
for a in array:
    print(a[0], a[1])