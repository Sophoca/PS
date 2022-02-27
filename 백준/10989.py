import sys
# 많은 수를 입력받을 때는 input()보다 readline() 함수 사용
# 계수정렬(Counting Sort)를 사용 -> 데이터의 범위가 적기 때문에 사용 가능

N=int(sys.stdin.readline())
array=[0]*10001
for _ in range(N):
    input_data=int(sys.stdin.readline())
    array[input_data]+=1
for i in range(10001):
    if array[i]!=0:
        for _ in range(array[i]):
            print(i)