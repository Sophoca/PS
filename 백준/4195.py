def find(x):
    if x==parent[x]:
        return x
    else:
        p=find(parent[x])
        parent[x]=p
        return p

def union(x, y):
    x=find(x)
    y=find(y)
    if x!=y:
        parent[y]=x
        number[x]+=number[y]

T=int(input())
for _ in range(T):
    F=int(input())
    parent=dict()
    number=dict()
    for _ in range(F):
        x, y=input().split(' ')
        if x not in parent:
            parent[x]=x
            number[x]=1
        if y not in parent:
            parent[y]=y
            number[y]=1
        union(x, y)
        print(number[find(x)])