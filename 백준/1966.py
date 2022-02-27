queue=[]
t=int(input())
while(t):
    N, M=list(map(int, input().split(' ')))
    count=0
    t-=1
    queue=list(map(int, input().split(' ')))
    queue=[(index, i) for index, i in enumerate(queue)]
    while True:
        if queue[0][1]==max(queue, key=lambda x:x[1])[1]:
            count+=1
            if queue[0][0]==M:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
