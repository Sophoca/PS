# stack 2개를 선언하여 커서를 기준으로 left, right stack 활용
t=int(input())
for _ in range(t):
    data=input()
    left, right=[], []
    for i in data:
        if i=='<':
            if left: 
                right.append(left.pop())
        elif i=='>':
            if right: 
                left.append(right.pop())
        elif i=='-':
            if left: 
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))


    # simulation 방식: cursor을 이동
    # key=input()
    # result=[]
    # idx=0
    # for i in key:
    #     if i=='<':
    #         if idx>0: idx-=1
    #     elif i=='>':
    #         if idx<len(result): idx+=1
    #     elif i=='-':
    #         if idx>0:
    #             result.pop(idx-1)
    #             idx-=1
    #     else:
    #         result.insert(idx, i)
    #         idx+=1
    # print(''.join(result))
