T = int(input())
for _ in range(T):
    N = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if N >= 3:
        for idx in range(3, N + 1):
            zero.append(zero[idx - 1] + zero[idx - 2])
            one.append(one[idx - 1] + one[idx - 2])
    print(zero[N], one[N])