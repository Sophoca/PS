# 재귀 사용시 시간초과 뜸
# def Z(n, x, y):
#     global value
#     if n==2:
#         if x==r and y==c:
#             print(value)
#             return
#         value+=1
#         if x==r and y+1==c:
#             print(value)
#             return
#         value+=1
#         if x+1==r and y==c:
#             print(value)
#             return
#         value+=1
#         if x+1==r and y+1==c:
#             print(value)
#             return
#         value+=1
#         return
#     Z(n/2, x, y)
#     Z(n/2, x, y+n/2)
#     Z(n/2, x+n/2, y)
#     Z(n/2, x+n/2, y+n/2)

N, r, c=map(int, input().split(' '))
value=0
while N>1:
    if r>=2**(N-1):
        if c>=2**(N-1):
            value+=3*(4**(N-1))
            c-=2**(N-1)
        else:
            value+=2*(4**(N-1))
        r-=2**(N-1)
    else:
        if c>=2**(N-1):
            value+=4**(N-1)
            c-=2**(N-1)
    N-=1

if r==1:
    if c==1:
        print(value+3)
    else:
        print(value+2)
else:
    if c==1:
        print(value+1)
    else:
        print(value)