def count():
    max=-1
    result=0
    for i in array:
        if i>max:
            max=i
            result+=1
    return result
        
N=int(input())
array=list()
for _ in range(N):
    array.append(int(input()))
print(count())
array.reverse()
print(count())