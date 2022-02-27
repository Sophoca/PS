mylist=[list(input()) for _ in range(8)]
sum=0
for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        if mylist[i][j]=='F':
            sum+=1
for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        if mylist[i][j]=='F':
            sum+=1
print(sum)
