ax, ay, bx, by, cx, cy=tuple(map(int, input().split()))
a, b, c=(ax, ay), (bx, by), (cx, cy)
def calc(x, y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
if (b[0]-a[0])*(c[1]-a[1])==(c[0]-a[0])*(b[1]-a[1]):
    print(-1)
else:
    print(2*(max(calc(a, b), calc(a, c), calc(b, c))-min(calc(a, b), calc(a, c), calc(b, c))))