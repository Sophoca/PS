# O(2^n) 시간복잡도를 가지기에 재귀함수로 해결하기엔 너무 오래걸림
# def fibo(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

N=int(input())
a, b=0, 1
while N>0:
    a, b=b, a+b
    N-=1
print(a)