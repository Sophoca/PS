N, M=map(int, input().split())
a=[input() for _ in range(N)]
b=[input() for _ in range(M)]
c=sorted(list(set(a)&set(b)))
print(len(c), '\n'.join(c), sep='\n')