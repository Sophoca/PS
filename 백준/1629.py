def mul(a, n):
    if n == 1:
        return a % C
    else:
        temp = mul(a, n//2)
        if n % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * a % C


A, B, C = map(int, input().split())
print(mul(A, B))
