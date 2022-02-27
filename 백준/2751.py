N=int(input())
array=list()
for _ in range(N):
    array.append(int(input()))
array.sort()
for i in array:
    print(i, end='\n')