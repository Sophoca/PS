import sys

N = int(input())
S = 0
for _ in range(N):
    oper = sys.stdin.readline().strip().split()
    if len(oper) == 1:
        if oper[0] == "all":
            S = (1 << 21) - 1
        elif oper[0] == "empty":
            S = 0
    else:
        data = int(oper[1])
        if oper[0] == "add":
            S |= 1 << data
        elif oper[0] == "check":
            print(1 if S & (1 << data) else 0)
        elif oper[0] == "remove":
            S &= ~(1 << data)
        elif oper[0] == "toggle":
            S ^= (1 << data)