N = int(input())
tree = {idx: [] for idx in range(1, N + 1)}
checked = [0] * (N + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b not in tree[a]:
        tree[a].append(b)
    if a not in tree[b]:
        tree[b].append(a)

stack = list()
stack.extend(tree[1])
checked[1] = 1
while stack:
    item = stack.pop()
    if not checked[item]:
        checked[item] = 1
        stack.extend(tree[item])

print(checked.count(1) - 1)
