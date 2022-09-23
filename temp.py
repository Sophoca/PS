A, B = map(int, input().split(' '))

isYT = True
while A < 5 and B < 5:
    if isYT:
        isYT = False
        B += A
    else:
        isYT = True
        A += B
print('yt' if B >= 5 else 'yj')