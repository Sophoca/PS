N, M=map(int, input().split(' '))
castle=list()
checkN=[0]*N
checkM=[0]*M
result=0
for _ in range(N):
    castle.append(input())
for i in range(N):
    for j in range(M):
        if castle[i][j]=='X':
            checkN[i]=1
            checkM[j]=1

print(max(checkM.count(0), checkN.count(0)))