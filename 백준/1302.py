N=int(input())
count=dict()
for i in range(N):
    bookName=input()
    if bookName not in count:
        count[bookName]=1
    else:
        count[bookName]+=1
count=sorted(count.items(), key=lambda x:x[0])
print(max(count, key=lambda x:x[1])[0])