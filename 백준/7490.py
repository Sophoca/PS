import copy

def operators(array, n):
    if len(array)==n:
        op_array.append(copy.deepcopy(array)) # deep copy를 해야 list값을 완전히 복사
        return
    array.append(' ')
    operators(array, n)
    array.pop()
    array.append('+')
    operators(array, n)
    array.pop()
    array.append('-')
    operators(array, n)
    array.pop()

t=int(input())
for _ in range(t):
    N=int(input())
    array=list(range(1, N+1))
    op_array=[]
    operators([], N-1)

    for op in op_array:
        result=''
        for i in range(N-1):
            result+=str(array[i])+op[i]
        result+=str(array[-1])
        if eval(result.replace(' ', ''))==0:    # eval을 통해 문자열 상태로 계산 가능
            print(result)
    print()