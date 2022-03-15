N, M = map(int, input().split())
table = {}
for idx in range(1, N + 1):
    name = input()
    table[idx] = name
    table[name] = idx
for _ in range(M):
    question = input()
    if question.isdecimal():
        print(table[int(question)])
    else:
        print(table[question])
