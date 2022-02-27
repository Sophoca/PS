N=int(input())
A=set(map(int, input().split(' ')))
M=int(input())
B=list(map(int, input().split(' ')))
for i in B:
    if i not in A:
        print(0)
    else:
        print(1)