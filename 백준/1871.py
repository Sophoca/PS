N=int(input())
for _ in range(N):
    input_data=list(input().split('-'))
    input_data[0]=list(input_data[0])
    sum=0
    for i in range(3):
        sum+=((ord(input_data[0][i])-ord('A'))*(26**(2-i)))
    sum-=int(input_data[1])
    if sum>=-100 and sum<=100:
        print('nice')
    else:
        print('not nice')